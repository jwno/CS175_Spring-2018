# CS175_Spring-2018
### Project Title: Hand Pose Estimation
### Project Number: Group 35

#### Project Description:
In this project, we used the YOLO, otherwise known as You Only Look Once, algorithm.  What this algorithm does is that it scans the entire image and detects different objects that are present within the image. We used this to our advantage to detect our hand in our picture.  Using the class dataset, we cropped the images to just the hands so that we could have YOLO detect hands in images. Using those images, the modified YOLO will intake the training and testing images, then correctly distinguish the hand pose for closed versus opened hand.

1) Hand Pose-GPU.ipynb: This is an ipynb that trains the classifiers and runs it as well to demonstrate the accuracy of our models.
2) Procses_all_data.ipynb: This is an ipynb that creates all the datasets (train/test,left/right,open/closed) we need to train the model.
3) load_and_run_model_gpu.ipynb: This is an ipynb that imports an already trained model and runs and demonstrate our model.
4) closed_hands.txt: This is a text file that contains the names of all the closed_hands images we will use for training.
5) left_right_model_gpu: This is an already trained model for the left and right hand classifier.
6) open_closed_model_gpu: This is an already trained model for the open and closed hand classifier.
