import os
import shutil

##USER EDIT START##

# Directories (Closed Hand, All Photo)
path_txt = r'C:\Users\JayNo\Desktop\data\test_hands.txt'

# Python creates new Folder.
# Give it a directory name: r'C:\Users\...\new_folder_directory_name'
datapath = r'C:\Users\JayNo\Desktop\data\hands'
newdirectory = r'C:\Users\JayNo\Desktop\data\new_directory'

##USER EDIT END##

if not os.path.exists(newdirectory):
    os.makedirs(newdirectory)

# Move file [jpg] from one folder to another
list_closed = []
with open(path_txt, 'r') as f:
    for filename in f.read().splitlines():
        filename = filename[filename.rfind('/')+1:]
        path = os.path.join(datapath, filename)
        shutil.move(path, newdirectory)

