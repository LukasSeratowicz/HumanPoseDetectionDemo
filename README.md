# Human Pose Estimation Demo

## Pre-Requirements:
- Computer (preferably with CUDA GPU)
- Python
Tested on Windows 11 with Python 3.11 and CUDA installed, using an RTX 3060 Mobile

## Requirements:
- Copy the repository or download and unzip the file
- Run `pip install -r requirements.txt` to install the following dependencies:
  a) OpenCV
  b) Ultralitycs
  c) NumPy
  d) PyTorch

Running on GPU is not necessary, but highly advised due to speed advantage. If you want to run on GPU, follow instructions below:

Please run `GPUcheck.py` to see if your GPU is available and is using CUDA.   
If the program reports the usage of CPU instead, you can install CUDA with the following link:  
[CUDA Installation Guide for Microsoft Windows](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)  
If you have CUDA installed but the program still reports CPU as the main device:
- Uninstall torch and torchvision
- Check what CUDA version you have using `nvcc --version`
- Install PyTorch with CUDA selected from the following link: [PyTorch Installation](https://pytorch.org/get-started/locally/)
<img src="https://github.com/LukasSeratowicz/HumanPoseDetectionDemo/assets/127187274/aed58a08-90af-4ebb-9bcf-dcb5739fe41f" alt="GPUcheck.py in action" width="350"/>


**Webcam not detected?**
- The most common issue is that you might be running it in a virtual machine that does not have direct access to your webcam.

### `image2image.py` - Image to Image
This program takes a picture and outputs an altered image.
 <br> 
<img src="https://github.com/LukasSeratowicz/HumanPoseDetectionDemo/assets/127187274/62426549-bbb3-4ae8-8641-b35745715ae4" alt="image2image in action PRE" width="350"/>

<img src="https://github.com/LukasSeratowicz/HumanPoseDetectionDemo/assets/127187274/1c459681-703d-4af6-be07-9c95b2ac633e" alt="image2image in action POST" width="350"/>

### `webcam.py` - Webcam Live Preview
Showcase of live abilities to detect human pose.
