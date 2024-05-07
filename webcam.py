from ultralytics import YOLO
import numpy as np
import cv2 as cv
import torch

# Check if running on CPU or GPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Running on {device}")
print(f"Using OpenCV v{cv.__version__}")
if (device == 'cuda'):
    print(f"Using GPU with Cuda v{torch.version.cuda}")

# Import model
print("Importing AI model...")
model = YOLO("yolov8n-pose.pt").to(device)
print("AI model imported")

# Get the camera
camera_id = 0 ### CHANGE THIS IF YOU HAVE MORE THAN 1 CAMERA
print(f"Turning on camera id: {camera_id}")
cap = cv.VideoCapture(camera_id)
if not cap.isOpened():
    print(f"Cannot open camera id: {camera_id}")
    exit()

# Get camera information
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# Main loop
while True:

    # Capture webcam data
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    #tests - read your own image instead
    #frame = cv.imread('soldiers.png')

    height, width, _ = frame.shape
    # Target dimensions
    target_size = 640

    # Calculate scaling factors for resizing
    scale = min(target_size / width, target_size / height)

    # Calculate new dimensions while preserving aspect ratio
    new_width = int(width * scale)
    new_height = int(height * scale)

    # Resize the frame
    resized_frame = cv.resize(frame, (new_width, new_height))

    # Create a black canvas with the target size
    canvas = np.zeros((target_size, target_size, 3), dtype=np.uint8)

    # Calculate the position to paste the resized frame with black bars
    start_x = (target_size - new_width) // 2
    start_y = (target_size - new_height) // 2
    end_x = start_x + new_width
    end_y = start_y + new_height

    # Paste the resized frame onto the canvas
    canvas[start_y:end_y, start_x:end_x] = resized_frame

    # Usage of AI model
    results = model(source=canvas, show=False, conf=0.3, save=False) #show=True makes it very laggy

    # Define connections between keypoints (indices of connected keypoints)
    connections = [
        (0, 1), (0, 2), (0, 5), (0, 6), (1, 3), (2, 4), (5, 6), (5, 7), (5, 11), (6, 8), (6, 12),
        (7, 9), (8, 10), (11, 12), (11, 13), (12, 14), (13, 15), (14, 16)
    ]

    for i in range(0, len(results[0].keypoints.xy)):
        keypoints = results[0].keypoints.xy[i]
        for keypoint in keypoints:
            x, y = keypoint
            if x != 0 and y != 0:
                cv.circle(canvas, (int(x), int(y)), 8, (238, 146, 194), 2)

        # Draw lines between keypoints
        if len(keypoints) != 0:
            for connection in connections:
                start_idx, end_idx = connection
                start_point = tuple(map(int, keypoints[start_idx]))
                end_point = tuple(map(int, keypoints[end_idx]))
                if start_point != (0, 0) and end_point != (0, 0):
                    cv.line(canvas, start_point, end_point, (238, 146, 194), 2)



    cv.imshow('Human Pose Detection DEMO webcam - q to exit', canvas)
    # print(blue_box_view)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()


