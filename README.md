Human Pose Estimation Demo

PreRequirements:
- Computer (preferably with CUDA installed)
- tested on Windows 11 python 3.11 with CUDA installed RTX 3060 Mobile
- Python installed

Requirements:
- Copy Repository, or download and uzip the file
- `pip install -r requirements.txt` - installs:
a) openCV
b) ultralitycs
c) numpy
d) torch

Check if you are Running on GPU:
please run `GPUcheck.py` to see if your GPU is available and is using CUDA.
If the program is reporting usage of CPU instead, you can install CUDA with the following link:
https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html
If you have CUDA installed, but the program still reports CPU as main device:
- Uninstall torch and pytorch
- Install pytorch with CUDA selected from the following link:
https://pytorch.org/get-started/locally/

Webcam not detected?
- Most common issue is you might be running it in a virtual machine, that does not have a direct access to your webcam.

`image2image.py` - Image to Image
This program takes a picture and outputs an altered image.

`webcam.py` - Webcam Live Preview
Showcase of live ablities to detect 
