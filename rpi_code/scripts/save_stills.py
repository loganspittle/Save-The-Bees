import cv2
import numpy as np

# Path to the video
video_path = 'Pictures/death_march.h264'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video is opened correctly
if not cap.isOpened():
    print("Error: Couldn't open the video.")
    exit()

# List of frame numbers to capture stills from (you can modify these)
frame_numbers = [55, 102, 220]  # Modify this with your desired frame numbers

# Counter for frame index
frame_count = 0

# Loop through the video frames
while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break  # Break if no more frames

    # If the current frame is one of the selected frame numbers, save it
    if frame_count in frame_numbers:
        # Save the frame as an image
        filename = f"frame_{frame_count}.png"
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")

        # Convert the frame to HSV
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # You can now analyze the HSV values of the image
        # For demonstration, we'll just calculate the mean HSV value
        mean_hue = np.mean(hsv_frame[:, :, 0])
        mean_saturation = np.mean(hsv_frame[:, :, 1])
        mean_value = np.mean(hsv_frame[:, :, 2])
        print(f"Frame {frame_count} - Mean HSV: ({mean_hue:.2f}, {mean_saturation:.2f}, {mean_value:.2f})")

    # Increment the frame count
    frame_count += 1

    # Stop when all selected frames are processed
    if frame_count > max(frame_numbers):
        break

# Release the video capture object
cap.release()

print("Done!")
