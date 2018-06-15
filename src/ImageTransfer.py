import os
import shutil

##USER EDIT START##

# Directories (Closed Hand, All Photo)
path_jpg = r'C:\Users\JayNo\Desktop\data\train_hand'

# Python creates new Folder.
# Give it a directory name: r'C:\Users\...\new_folder_directory_name'
newpath = r'C:\Users\JayNo\Desktop\data\new_directory'

##USER EDIT END##


if not os.path.exists(newpath):
    os.makedirs(newpath)

# Move file [jpg] from one folder to another
list_closed = []
for filename in os.listdir(path_jpg):
    if (filename[-3:] == "jpg"):
        path = os.path.join(path_jpg, filename)
        shutil.move(path, newpath)
