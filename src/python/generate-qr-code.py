import qrcode

data = "https://instagram.com/pure.python"

fileName = "images/pure-python-url.png"

img = qrcode.make(data)

img.save(fileName)


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread(fileName)
imgplot = plt.imshow(img)
plt.show()

