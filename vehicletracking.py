import cv2
import torch
import numpy as np

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Initialize video capture
cap = cv2.VideoCapture('/Users/macyk/Downloads/DJI_0107.MP4')  # Replace with your video file path

# Define a function to draw bounding boxes
def draw_boxes(frame, boxes):
    for box in boxes:
        x1, y1, x2, y2, conf, cls = box
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, f'Vehicle {conf:.2f}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame to improve performance
    img = cv2.resize(frame, (640, 480))

    # Perform detection
    results = model(img)

    # Process results
    boxes = []
    for *box, conf, cls in results.xyxy[0].tolist():
        if int(cls) == 2:  # Class 2 is for cars in COCO dataset
            boxes.append([*box, conf, cls])

    # Draw bounding boxes on the original frame
    draw_boxes(frame, boxes)

    # Display the frame
    cv2.imshow('Vehicle Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
