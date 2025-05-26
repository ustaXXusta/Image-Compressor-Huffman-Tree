# 🖼️ Image Compression & Huffman Tree Visualization

This repository provides two Python scripts for image compression and Huffman tree visualization. Compress images efficiently or visualize Huffman trees in a command-line interface (CLI) with ease! 🚀

---

## 📋 Overview

The repository includes:

- **`p.py`**: Compresses images using 1/2 scaling, quantization, and Huffman coding.  
- **`huffman.py`**: Generates and displays a Huffman tree for an image in a CLI UI.

---

## 📂 Files

| File         | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `p.py`       | Compresses images by applying 1/2 scaling, quantization, and Huffman coding.|
| `huffman.py` | Builds and visualizes a Huffman tree based on image pixel frequencies in CLI.|

---

## 🔧 Features

### `p.py`

- **1/2 Scaling**: Halves image dimensions to reduce data size.  
- **Quantization**: Simplifies pixel values for efficient storage.  
- **Huffman Coding**: Encodes data using a Huffman tree for optimal compression.

### `huffman.py`

- **Tree Generation**: Creates a Huffman tree from pixel intensity frequencies.  
- **CLI Visualization**: Displays the tree structure in a text-based interface.

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x  
- Libraries: `Pillow`, `numpy` (optional)

Install dependencies:
```bash
pip install pillow numpy
