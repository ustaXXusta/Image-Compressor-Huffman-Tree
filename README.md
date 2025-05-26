Image Compression and Huffman Tree Visualization
This repository contains two Python scripts for image compression and Huffman tree visualization:

p.py: A script for compressing images by applying 1/2 scaling, quantization, and Huffman coding to reduce file size while maintaining acceptable quality.
huffman.py: A script that generates a Huffman tree for any input image and visualizes it in a CLI-based user interface.

Files
p.py
This script implements image compression using the following techniques:

1/2 Scaling: Reduces the image dimensions by half to decrease data size.
Quantization: Reduces the number of distinct pixel values to simplify the data.
Huffman Coding: Encodes pixel data using a Huffman tree for efficient compression.

huffman.py
This script focuses on Huffman coding:

Generates a Huffman tree based on pixel intensity frequencies of an input image.
Displays the Huffman tree structure in a CLI-based user interface for easy visualization.

Usage

Requirements: Ensure you have Python 3.x installed, along with dependencies like Pillow for image processing and any other required libraries (e.g., numpy).
Running p.py: Use python p.py <image_path> to compress an image.
Running huffman.py: Use python huffman.py <image_path> to generate and visualize the Huffman tree in the CLI.

Notes

Ensure input images are in a supported format (e.g., PNG, JPEG).
The compression in p.py balances quality and file size; adjust quantization levels in the script for different results.
The CLI visualization in huffman.py provides a text-based representation of the Huffman tree.

