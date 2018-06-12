import os
import shutil

##USER EDIT START##

# Directories (Closed Hand, All Photo)
path_close = r'C:\Users\user1\Desktop\Data\Closed'
path_all = r'C:\Users\user1\Desktop\Data\All'

# Python creates new Folder.
# Give it a directory name: r'C:\Users\...\new_folder_directory_name'
newpath = r'C:\Users\user1\Desktop\Data\Open'

##USER EDIT END##

# Get "closed hand" file directory name
list_closed = []
for filename in os.listdir(path_close):
    list_closed.append(filename)

# Get "open hand" file directory name
list_open = []
for filename in os.listdir(path_all):
    if (filename not in list_closed):
        list_open.append(filename)

# Create Folder
if not os.path.exists(newpath):
    os.makedirs(newpath)

# Copy Open Hand to newpath
for filename in list_open:
    path = os.path.join(path_all, filename)
    shutil.copy(path, newpath)
