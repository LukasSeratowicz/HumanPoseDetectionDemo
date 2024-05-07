import cv2 as cv
import torch
import tkinter as tk
from tkinter import messagebox

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Running on {device}")
print(f"Using OpenCV v{cv.__version__}")
if device == 'cuda':
    print(f"Using GPU with Cuda v{torch.version.cuda}")

# Create a Tkinter window
root = tk.Tk()
root.withdraw()

popup_text = f"Running on {device.upper()} with OpenCV v{cv.__version__}\n"

if device != 'cuda':
    messagebox.showwarning("GPU check - NO GPU DETECTED!", popup_text)
else:
    popup_text += f"Cuda v{torch.version.cuda}"
    messagebox.showinfo("GPU check - detected", popup_text)

root.destroy()