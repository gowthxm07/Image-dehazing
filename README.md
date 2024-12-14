# Image Dehazing Using Image Decomposition

This project aims to enhance images by applying image decomposition techniques to separate and enhance different layers such as **structure**, **texture**, and **glow**. The final result is a dehazed image created by blending these layers in a realistic manner.

## Project Overview

This project uses Python and several libraries, including **PIL**, **NumPy**, and **Matplotlib**, to process and dehaze an image. The process involves the following steps:
1. **Image Decomposition**: The image is decomposed into different layers: structure, texture, and glow.
2. **Layer Enhancement**: The structure layer is enhanced using contrast stretching to improve the clarity and details.
3. **Layer Blending**: The enhanced structure layer is blended with the texture layer using a weighted average to produce a final dehazed image.

## Features

- **Grayscale Conversion**: Converts input images to grayscale for better processing.
- **Gaussian Filtering**: Applies Gaussian filters to extract structure, texture, and glow layers.
- **Contrast Stretching**: Enhances the structure layer to improve visual quality.
- **Realistic Blending**: Combines the enhanced structure and texture layers to form a dehazed, visually appealing image.

## Requirements

- Python 3.x
- PIL (Pillow)
- NumPy
- Matplotlib

You can install the required libraries using the following command:

```bash
pip install pillow numpy matplotlib
