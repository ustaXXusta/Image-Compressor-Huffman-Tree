import cv2
import numpy as np
import os
from collections import Counter
import heapq

# Huffman kodlaması için yardımcı sınıflar ve fonksiyonlar
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_kodlama(piksel_degerleri):
    # Piksel değerlerinin frekanslarını hesapla
    frekanslar = Counter(piksel_degerleri.flatten())
    if len(frekanslar) <= 1:
        return {list(frekanslar.keys())[0]: '0'}, piksel_degerleri
    
    # Huffman ağacını oluştur
    heap = []
    for symbol, freq in frekanslar.items():
        heapq.heappush(heap, Node(freq, symbol))
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        for direction in [(left, '0'), (right, '1')]:
            direction[0].huff = direction[1]
        heapq.heappush(heap, Node(left.freq + right.freq, None, left, right))
    
    # Huffman kodlarını oluştur
    huffman_kodlari = {}
    def generate_codes(node, code=''):
        if node is None:
            return
        if node.symbol is not None:
            huffman_kodlari[node.symbol] = code if code else '0'
        generate_codes(node.left, code + '0')
        generate_codes(node.right, code + '1')
    
    root = heap[0]
    generate_codes(root)
    
    return huffman_kodlari, piksel_degerleri

def goruntu_sikistir(giris_yolu, cikis_yolu, kucultme_orani=0.5, renk_seviyesi=16, jpg_kalitesi=50):
    # Görüntüyü oku
    goruntu = cv2.imread(giris_yolu)
    if goruntu is None:
        print("Hata: Görüntü dosyası bulunamadı!")
        return

    # Orijinal görüntü bilgileri
    print(f"Orijinal görüntü şekli (shape): {goruntu.shape}")
    print(f"Orijinal görüntü veri tipi: {goruntu.dtype}")

    # 1. Görüntüyü küçült (alt örnekleme)
    yukseklik, genislik = goruntu.shape[:2]
    yeni_yukseklik = int(yukseklik * kucultme_orani)
    yeni_genislik = int(genislik * kucultme_orani)
    kucuk_goruntu = cv2.resize(goruntu, (yeni_genislik, yeni_yukseklik), interpolation=cv2.INTER_AREA)
    print(f"Küçültülmüş görüntü şekli: {kucuk_goruntu.shape}")
    print(f"Küçültme oranı: {kucultme_orani}")
    print(f"Yeni yükseklik: {yeni_yukseklik}, Yeni genişlik: {yeni_genislik}")

    # 2. Renk sayısını azalt (kuantizasyon)
    goruntu_float = kucuk_goruntu.astype(np.float32)
    print(f"Float'a çevrilmiş görüntü veri tipi: {goruntu_float.dtype}")
    kuantize_goruntu = np.floor(goruntu_float / (256 / renk_seviyesi)) * (256 / renk_seviyesi)
    kuantize_goruntu = kuantize_goruntu.astype(np.uint8)
    print(f"Kuantize edilmiş görüntü veri tipi: {kuantize_goruntu.dtype}")
    print(f"Renk seviyesi: {renk_seviyesi}")

    # 3. Huffman kodlaması uygula
    print("Huffman kodlaması uygulanıyor...")
    huffman_kodlari, kuantize_goruntu = huffman_kodlama(kuantize_goruntu)
    print("Huffman kodları oluşturuldu:", huffman_kodlari)

    # 4. JPEG olarak kaydet (Huffman kodlaması zaten JPEG içinde var, ama biz ek bir katman olarak simüle ettik)
    cv2.imwrite(cikis_yolu, kuantize_goruntu, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_kalitesi])
    print(f"JPEG kalitesi: {jpg_kalitesi}")

    # Dosya boyutlarını göster
    orijinal_boyut = os.path.getsize(giris_yolu) / 1024  # KB
    sikistirilmis_boyut = os.path.getsize(cikis_yolu) / 1024  # KB
    print(f"Orijinal boyut: {orijinal_boyut:.2f} KB")
    print(f"Sıkıştırılmış boyut: {sikistirilmis_boyut:.2f} KB")
    print(f"Sıkıştırma oranı: {orijinal_boyut / sikistirilmis_boyut:.2f}x")

def main():
    # Kendi test görüntüm
    giris_goruntu = "ucak.jpg"  
    cikis_goruntu = "yeni_goruntu.jpg"

    try:
        goruntu_sikistir(giris_goruntu, cikis_goruntu)
        print(f"Sıkıştırılmış görüntü '{cikis_goruntu}' olarak kaydedildi!")
    except Exception as hata:
        print(f"Bir şeyler ters gitti: {hata}")

if __name__ == "__main__":
    main()