import cv2

# Read the image
image = cv2.imread('/Users/macyk/Downloads/Images/DJI7_frame_1.jpg')

# Get the dimensions
height, width, channels = image.shape
print(f"Width: {width}, Height: {height}, Channels: {channels}")
