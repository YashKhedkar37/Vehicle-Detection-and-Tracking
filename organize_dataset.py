import os
import shutil


# List of image and corresponding label filenames
filenames = [
    ("DJI7_frame_1.jpg", "DJI7_frame_1.txt"),
    ("DJI7_frame_2000.jpg", "DJI7_frame_2000.txt"),
    ("DJI7_frame_3000.jpg", "DJI7_frame_3000.txt"),
    ("DJI7_frame_4000.jpg", "DJI7_frame_4000.txt"),
    ("DJI7_frame_6000.jpg", "DJI7_frame_6000.txt"),
    ("DJI7_frame_7000.jpg", "DJI7_frame_7000.txt"),
    ("DJI8_frame_1.jpg", "DJI8_frame_1.txt"),
    ("DJI8_frame_5995.jpg", "DJI8_frame_5995.txt"),
    ("DJI9_frame_4000.jpg", "DJI9_frame_4000.txt"),
    ("DJI9_frame_5000.jpg", "DJI9_frame_5000.txt"),
]

# Split data into training and validation sets
train_files = filenames[:5]
val_files = filenames[5:]

# Move files to respective directories
for image, label in train_files:
    shutil.move(image, f'dataset/images/train/{image}')
    shutil.move(label, f'dataset/labels/train/{label}')

for image, label in val_files:
    shutil.move(image, f'dataset/images/val/{image}')
    shutil.move(label, f'dataset/labels/val/{label}')
