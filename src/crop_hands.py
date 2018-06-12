import cv2
import numpy as np
import json

# This is the path to where your annotation.json file is from the class dataset you download
with open('C:\\Users\\515852\\Documents\\Nathan\\CS175\\hand_pose\\Dataset\\annotation.json') as data_file:
    data = json.load(data_file)

# This is the path to the directory where all the images are
path = 'C:\\Users\\515852\\Documents\\Nathan\\CS175\\hand_pose\\Dataset\\Color\\'
for each in data:
    min_y = data[each][0][1]
    max_y = data[each][0][1]
    min_x = data[each][0][0]
    max_x = data[each][0][0]
    
    for pair in data[each]:
        if pair[1] < min_y:
            min_y = pair[1]
        if pair[1] > max_y:
            max_y = pair[1]
        if pair[0] < min_x:
            min_x = pair[0]
        if pair[0] > max_x:
            max_x = pair[0]
    
    file_name = each[:-2]+".jpg"
    full_path = path+file_name
    img = cv2.imread(full_path)
    
    y_add = 200-(int(max_y)-int(min_y))
    x_add = 200-(int(max_x)-int(min_x))

    min_x = int(min_x)
    min_y = int(min_y)
    max_x = int(max_x)
    max_y = int(max_y)
    
    if y_add % 2 == 0:
        y_cord_min = max(0,min_y - int(y_add/2))
        y_cord_max = min(1080,max_y + int(y_add/2))

    else:
        y_cord_min = max(0,min_y - (1+int(y_add/2)))
        y_cord_max = min(1080,max_y + int(y_add/2))

    if x_add % 2 == 0:
        x_cord_min = max(0,min_x - int(x_add/2))
        x_cord_max = min(1920,max_x + int(x_add/2))

    else:
        x_cord_min = max(0,min_x - (1+int(x_add/2)))
        x_cord_max = min(1920,max_x + int(x_add/2))
    
    output = "hands\\"+each+".jpg"
    pixels = img[y_cord_min:y_cord_max,x_cord_min:x_cord_max]
    
    cv2.imwrite(output,pixels)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
