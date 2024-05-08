from ultralytics import YOLO
import cv2 as cv
import torch
import tkinter as tk
from tkinter import filedialog
import os

# Check if running on CPU or GPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Running on {device}")
print(f"Using OpenCV v{cv.__version__}")
if(device == 'cuda'):
    print(f"Using GPU with Cuda v{torch.version.cuda}")

# get file and display preview
file_path = None
from PIL import ImageTk, Image
def open_file():
    global image_preview_label
    program_directory = os.path.dirname(os.path.realpath(__file__))
    initial_dir = os.path.abspath(program_directory)
    file_path = filedialog.askopenfilename(initialdir=initial_dir,filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image = Image.open(file_path)
        screen_width = root.winfo_screenwidth() - 50  # Subtract 50 pixels for padding
        screen_height = root.winfo_screenheight() - 100  # Subtract 100 pixels for padding and button
        if image.width > screen_width or image.height > screen_height:
            image.thumbnail((screen_width*8/10, screen_height*8/10))
        #image = image.resize((640, 640))
        image_preview = ImageTk.PhotoImage(image)
        image_preview_label.configure(image=image_preview)
        image_preview_label.image = image_preview
        process_button.config(state=tk.NORMAL)
        process_button["command"] = lambda: processing(file_path)
        root.geometry(f"{image.size[0]}x{image.size[1] + 75}")

# AI Image processing - here is where the magic happens
def processing(file_path):
    if file_path == None:
        file_path="soldiers.png"
        print(f"No image selected, using default: {file_path}")
    print(f"Processing image: {file_path}")
    model = YOLO("yolov8n-pose.pt")
    results = model(source=file_path, show=True, conf=0.3, save=False) # Show the Results, but do not save

    # Example usage : Pick the first person and display all of their Joints - Keypoints
    image = cv.imread(file_path)

    screen_width = root.winfo_screenwidth() * 9 / 10
    screen_height = root.winfo_screenheight() * 9 / 10
    # Resize the image for displaying if it is too big
    scale_factor = 1
    if image.shape[1] > screen_width or image.shape[0] > screen_height:
        scale_factor = min(screen_width / image.shape[1], screen_height / image.shape[0])
        image = cv.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv.INTER_LINEAR)

    keypoints = results[0].keypoints.xy[0]
    for keypoint in keypoints:
        x, y = keypoint
        print(f"keypoint - {keypoint}: x={x*scale_factor}  y={y*scale_factor}")
        if x != 0 and y != 0:
            cv.circle(image, (int(x*scale_factor), int(y*scale_factor)), 4, (0, 255, 0), 2)

    cv.imshow("Example usage : Pick the one person and display all of their Joints/Keypoints", image)
    cv.waitKey(0)
    cv.destroyAllWindows()


# Create Window and UI using Tinker
root = tk.Tk()
root.title("Human Pose Detection DEMO image2image")
root.geometry("450x100")

image_preview_label = tk.Label(root)
image_preview_label.pack()

open_button = tk.Button(root, text="Open Image", command=open_file)
open_button.pack()

process_button = tk.Button(root, text="Process", command=lambda: processing(file_path))
process_button.pack()

root.mainloop()

