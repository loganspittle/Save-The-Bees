import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
# img = cv2.imread('Pictures/Mite1.jpg')
img = cv2.imread('Pictures/frame_360.png')

# Convert the image to HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for red color in HSV
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])

# Create masks for red color
mask = cv2.inRange(hsv_img, lower_red1, upper_red1)
# mask2 = cv2.inRange(hsv_img, lower_red2, upper_red2)

# mask = cv2.bitwise_or(mask1, mask2)

# Find contours
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

# Convert the image from BGR to RGB for Matplotlib
img_contours_rgb = cv2.cvtColor(img_contours, cv2.COLOR_BGR2RGB)

# Display the image with contours using Matplotlib
# plt.imshow(img_contours_rgb)
# plt.axis('off')  # Turn off axis for better visualization
# plt.show()

def nothing(x):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('H_min', 'image', 0, 179, nothing)
cv2.createTrackbar('H_max', 'image', 0, 179, nothing)
cv2.createTrackbar('S_min', 'image', 0, 255, nothing)
cv2.createTrackbar('S_max', 'image', 0, 255, nothing)
cv2.createTrackbar('V_min', 'image', 0, 255, nothing)
cv2.createTrackbar('V_max', 'image', 0, 255, nothing)

while True:
    h_min = cv2.getTrackbarPos('H_min', 'image')
    h_max = cv2.getTrackbarPos('H_max', 'image')
    s_min = cv2.getTrackbarPos('S_min', 'image')
    s_max = cv2.getTrackbarPos('S_max', 'image')
    v_min = cv2.getTrackbarPos('V_min', 'image')
    v_max = cv2.getTrackbarPos('V_max', 'image')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv_img, lower, upper)
    cv2.imshow('image', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
