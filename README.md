# Human Pose Estimation Demo

## Pre-Requirements:
- Computer (preferably with CUDA installed)
- Tested on Windows 11 with Python 3.11 and CUDA installed, using an RTX 3060 Mobile
- Python installed

## Requirements:
- Copy the repository or download and unzip the file
- Run `pip install -r requirements.txt` to install the following dependencies:
  a) OpenCV
  b) Ultralitycs
  c) NumPy
  d) PyTorch

Running on GPU is not necessary, but highly advised due to the speed advantage. If you want to run on GPU, follow the instructions below:

Please run `GPUcheck.py` to see if your GPU is available and is using CUDA.   
If the program reports the usage of CPU instead, you can install CUDA with the following link:  
[CUDA Installation Guide for Microsoft Windows](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)  
If you have CUDA installed but the program still reports CPU as the main device:
- Uninstall torch and torchvision
- Check what CUDA version you have using `nvcc --version`
- Install PyTorch with CUDA selected from the following link: [PyTorch Installation](https://pytorch.org/get-started/locally/)

**Webcam not detected?**
- The most common issue is that you might be running it in a virtual machine that does not have direct access to your webcam.

### `image2image.py` - Image to Image
This program takes a picture and outputs an altered image.

### `webcam.py` - Webcam Live Preview
Showcase of live abilities to detect.
