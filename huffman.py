import cv2
import numpy as np
from collections import Counter
import heapq

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
        return {list(frekanslar.keys())[0]: '0'}, None
    
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
    return huffman_kodlari, root

def ciz_agac(node, seviye=0, prefix="Root: "):
    if node is not None:
        print("  " * seviye + prefix + str(node.symbol) + " (freq: " + str(node.freq) + ")")
        ciz_agac(node.left, seviye + 1, "L: ")
        ciz_agac(node.right, seviye + 1, "R: ")

def main():
    # Resim dosyasını oku (kendi resminizi belirtin)
    resim_yolu = "ev.jpg"  # Resim yolunu buraya yazın
    goruntu = cv2.imread(resim_yolu)
    if goruntu is None:
        print("Hata: Görüntü dosyası bulunamadı!")
        return

    # Piksel değerlerini al (örneğin, YCbCr dönüşümü olmadan direkt RGB'den)
    piksel_degerleri = goruntu.astype(np.uint8)

    # Huffman kodlamasını uygula
    huffman_kodlari, root = huffman_kodlama(piksel_degerleri)
    print("Huffman Kodları:", huffman_kodlari)
    print("\nHuffman Ağacı:")
    ciz_agac(root)

if __name__ == "__main__":
    main()