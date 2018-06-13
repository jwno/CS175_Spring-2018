import os
import shutil
from random import randint

##USER EDIT START##

# Directories with Open and Closed File
path_open = r'C:\Users\user1\Desktop\Data\Open'
path_close = r'C:\Users\user1\Desktop\Data\Closed'


# CREATE NEW FOLDER ON PYTHON
# Open Path
path_test_O = r'C:\Users\user1\Desktop\Data\TestOpen'
path_valid_O = r'C:\Users\user1\Desktop\Data\ValidOpen'

# Close Path
path_test_C = r'C:\Users\user1\Desktop\Data\TestClose'
path_valid_C = r'C:\Users\user1\Desktop\Data\ValidClose'

# Percentage(%)
test = 20

##USER EDIT END##


if not os.path.exists(path_test_O):
    os.makedirs(path_test_O)
        
if not os.path.exists(path_valid_O):
    os.makedirs(path_valid_O)

if not os.path.exists(path_test_C):
    os.makedirs(path_test_C)
        
if not os.path.exists(path_valid_C):
    os.makedirs(path_valid_C)
    

paths = [path_open, path_close]
path_list = [[path_test_O, path_valid_O,], [path_test_C, path_valid_C,]]
for i, path in enumerate(paths):
    list_path = []
    for filename in os.listdir(path):
        list_path.append(filename)

    takeout = int(len(list_path)*(test*0.01))
    for j in range(takeout):
        random_number = randint(0, len(list_path)-1)
        newpath = os.path.join(path, list_path[random_number])
        shutil.copy(newpath, path_list[i][0])
        del list_path[random_number]

    for j in list_path:
        newpath = os.path.join(path, j)
        shutil.copy(newpath, path_list[i][1])


