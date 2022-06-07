# 50.035CV-C01-Team10-Visual-Interactive-Game

## Model Preparation
1. Ensure that you have torch, torchvision, opencv, numpy and Pillow libraries installed.
2. change directory to the `Hand_Detection_YOLOv5` folder. 
3. run `git clone https://github.com/ultralytics/yolov5.git`

## Dataset
1. Download the FreiHAND dataset from https://lmb.informatik.uni-freiburg.de/resources/datasets/FreihandDataset.en.html
2. Extract the zip file into the `Hand_Pose_Estimation_2D` folder and name it as "FreiHAND_pub_v2"

## Training models
For training of the YOLOv5 model, follow the steps below:

1. Change directory to the local repository of yolov5 which we have cloned earlier
2. run `python train.py --data <path to yaml file> --batch <number of batches> --epochs <number of epochs> --weights yolov5m.pt`  

For training of the Hand Pose Estimation model, follow the steps below:

1. Change directory to `Hand_Pose_Estimation_2D` folder
2. Run all the cells within `Train.ipynb` (takes approximately 6 hours for training)
3. Evaluate the model performance by running cells in `Inference.ipynb`

## Usage of trained models

### Final prototype (Objection detection + Handpose Estimation)
To use the final model that incorporates both object detection and handpose estimation techniques, perform the following steps:

1. Change directory to `Hand_Detection_YOLOv5` folder
2. Run cells in `demo.ipynb`

### Final prototype (Using Mediapipe)
To use the final model that leverages on MediaPipe, perform the following steps:

1. change directory to `mediapipedrums` folder
2. run `demo.py`


### Running the application
It is recommended that you carry out these steps in Visual Studio Code. In the command line terminal, ensure that you are in the 50.035CV-C01-Team10-Visual-Interactive-Game folder. Then, execute the following steps:

1. Create a virtual environment
* POSIX: `python3 -m venv venv`
* Windows: `py -3 -m venv venv`

2. Activate the virtual environment
* POSIX: `. venv/bin/activate`
* Windows: `venv\Scripts\activate`

3. Install dependencies in the virtual environment  
`pip install -r requirements.txt`

4. Change directory to ***\<~/mediapipedrums>*** folder  
`cd mediapipedrums`

5. Run ***demo.py*** file  
`python demo.py`




