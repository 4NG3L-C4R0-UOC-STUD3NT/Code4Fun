import numpy as np
import cv2
import pyautogui
import uuid

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
fileName = "images/screenshot-{}.png".format(uuid.uuid4().hex)
print(fileName)
cv2.imwrite(fileName, image)



import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#plt.figure()
#plt.imshow(image) 
#plt.show()

img = mpimg.imread(fileName)
imgplot = plt.imshow(img)
plt.show()