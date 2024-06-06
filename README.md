
# Vehicle Tracking with YOLOv5:

This project involves training and deploying a YOLOv5 model for vehicle tracking in videos. The model is trained on a custom dataset to detect and track multiple classes of vehicles such as Auto, Bike, Car, Icv, Bus, Truck. The trained model is capable of processing high resolution images and videos and generating annotated outputs showing detected vehicles.

## Table of Contents
- [Introduction](#intro)
- [Installation](#installation)
- [Dataset](#dataset)
- [Training the Model](#training)
- [Inference](#inference)
- [Video Processing](#video-processing)
- [Results](#results)




## Introduction

YOLO (You Only Look Once) is a state-of-the-art, real-time object detection system. This project uses the YOLOv5 version to perform vehicle detection and tracking. The YOLOv5 model is trained on a custom dataset of vehicle images to detect and classify different types of vehicles.
## Installation

To run this project, you need to have Python 3.6 or higher installed. Follow the steps below to set up the environment and dependencies:

#### Downloading YOLOv5:


Clone the repository:

```bash
git clone https://github.com/ultralytics/yolov5.git
cd <repository_directory>
```
Install dependencies:

Install the required Python packages.
```bash
pip install -r requirements.txt
```
Install PyTorch:

Depending on your system and preferences (CPU or GPU), follow the instructions at [PyTorch]().



### Dataset:

The dataset used for training the YOLOv5 model consists of images annotated with bounding boxes for different vehicle classes. The annotations are in the YOLO format. The dataset needs to be structured in the following format:

```bash
/dataset
    /images
        /train
            - image1.jpg
            - image2.jpg
            ...
        /val
            - image1.jpg
            - image2.jpg
            ...
    /labels
        /train
            - image1.txt
            - image2.txt
            ...
        /val
            - image1.txt
            - image2.txt
            ...
```

Each .txt file contains the bounding box annotations for the corresponding image in YOLO format as:

```bash
class_id x_center y_center width height
```



### Training the Model

To train the YOLOv5 model on your custom dataset, follow these steps:

Prepare the Dataset:
Ensure your dataset is structured as described in the Dataset section.

Modify the YAML File:
Create a .yaml file (e.g., custom_data.yaml) with the dataset paths and class names:

```bash
train: /path/to/dataset/images/train
val: /path/to/dataset/images/val

nc: 6 # number of classes
names: ['Auto', 'Bike', 'Car', 'Icv', 'Bus', 'Truck']
```

Run Training:
```bash
python train.py --img 3840 --batch 2 --epochs 60 --data /path/to/custom_data.yaml --weights yolov5s.pt --cache
```


## Inference :

The model detects vehicles in images with high resolution (3840x2160) with high accuracy. Here are some examples of the output:

![TrainingData](NewFolder/train_batch0.jpg)
![TrainingData](NewFolder/train_batch2.jpg)


## Running Tests


- To run inference on a single image using the trained model:

Run Inference:

```bash
python detect.py --weights /path/to/best.pt --source /path/to/image.jpg --img 3840 --conf 0.25
```
View Results:
The output will be saved in the runs/detect/exp directory.




- To run inference on a video using the trained model:
```bash
python detect.py --weights /path/to/best.pt --source /path/to/video.mp4 --img 640 --conf 0.25
```

View Results:
The output video with annotations will be saved in the runs/detect/exp directory.


## Results
The random image after processing:
![Tracked_Vehicles](newFolder/checking.png)
