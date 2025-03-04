import cv2
import numpy as np

# Path to the input video
video_path = 'Pictures/video_output.h264'
video_path = 'Pictures/death_march.h264'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video is opened correctly
if not cap.isOpened():
    print("Error: Couldn't open the video.")
    exit()

# Define the codec and create a VideoWriter object to save the output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter('output_video.avi', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

# List of frame numbers to capture stills from (you can modify these)

# Counter for frame index

# Loop through the video frames
while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break  # Break if no more frames

    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define the range of green color to mask the background
    # GREEN
    # lower_green = np.array([35, 40, 40])
    # upper_green = np.array([85, 255, 255])
    # PURPLE
    lower_green = np.array([140, 0, 0])
    upper_green = np.array([162, 255, 255])
    
    # Create a mask for the green background
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    # Invert the mask to keep only the bees
    mask = cv2.bitwise_not(mask)
    
    # Apply the mask to the frame to remove the green background
    result = cv2.bitwise_and(frame, frame, mask=mask)


    # Convert result to grayscale for blob detection
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    
    # Threshold the image
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    
    # Find contours (alternative to blob detection)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw bounding boxes around detected objects
    for contour in contours:
        if cv2.contourArea(contour) > 5000:  # Filter small contours
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Write the processed result to the output video
    output_video.write(result)

    # Show the processed result in a window (for live visualization)
    cv2.imshow('Bees Detection', result)

# Release resources
cap.release()
output_video.release()
cv2.destroyAllWindows()

print("Done! Video saved as 'output_video.avi'")
