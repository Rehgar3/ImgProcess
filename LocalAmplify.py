import os
import cv2
import numpy as np

image = cv2.imread('./processedimage.png')

# First partial zoom
(x1,y1)=(25,150)
(x2,y2)=(160,275)
pt1 = (x1,y1)  # Rectangle box top left coordinates
pt2 = (x2,y2)  # Rectangle box bottom right coordinates
cv2.rectangle(image, pt1, pt2, (0, 0, 255), 2)
patch1 = image[y1:y2+1, x1:x2+1, :]
patch1 = cv2.resize(patch1, (200, 120))

# Second partial zoom
(x3,y3)=(180,130)
(x4,y4)=(265,195)
pt1 = (x3,y3)  # Rectangle box top left coordinates
pt2 = (x4,y4)  # Rectangle box bottom right coordinates
cv2.rectangle(image, pt1, pt2, (0, 255, 0), 2)
patch2 = image[y3:y4+1, x3:x4+1, :]
patch2 = cv2.resize(patch2, (200, 120))

# stack
#patch = np.hstack((patch1, patch2))
#image = np.vstack((image, patch))
#cv2.imshow('demo', image)

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

ensure_dir('F:/res/Amplify/')

cv2.imwrite('F:/res/Amplify/0.png', image)
cv2.imwrite('F:/res/Amplify/1.png', patch1)
cv2.imwrite('F:/res/Amplify/2.png', patch2)
