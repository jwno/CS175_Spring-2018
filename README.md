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

***IMPORTANT***
If you would like to train the model, please make sure to edit and run “Process_all_data.ipynb”.  The first edit is in the 2nd cell regarding the annotation.json file.  Please change the filepath to the filepath of the annotation.json file on your local computer.  The second edit is in the 3rd cell regarding the class dataset directory.  Change the variable named path to reflect the location of the images of all the hands from our class dataset.  After making these changes, please delete the directories: open_closed_test and right_left_test as these are actually smaller samples of our test data, made so that we could make our submission 5 MB or less.  By running the “Process_all_data.ipynb” you will be able to create the full test dataset, along with all the training data as well.

After you have made these changes, you can now run all cells and it will create all required directories for training.  The name of the directories that should be created are as follows: small_dataset, right_left_test, right_left_train, Opened, Closed, open_closed_test, and open_closed_train.

After running the “Process_all_data.ipynb” you can now run the “Hand Pose-GPU.ipynb” to train the model as well as see how the model performs by running all cells.  At the end, the ipynb will also export the trained models.
***IMPORTANT***

If you decide not to train the model, please download our pre-trained models on our github <https://github.com/piemastr2/CS175_Spring-2018>.  The pre-trained models are named “left_right_model_gpu” and “open_closed_model_gpu.” After you download the models to the same folder as “load_and_run_model_gpu.ipynb”, you can simply open up “load_and_run_model_gpu.ipynb” and by running all cells, it will import the trained models and show the model in action.  In the case, these instructions don’t lead to expected behavior, please follow the instructions on training the model and it will lead to the desired behavior.

