import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy
import math

image = "ddd.png"

# RGB(3 streams) matrix representation of the image
labrat = mpimg.imread(image)
print(labrat)

"""

Write the script wrt the given instruction here.

Define a threshold or a limit, (for example (160,160,160)) and if the RGB values of a pixel at a certain position in your chosen image is all greater than the threshold, then consider it to be typeA, else typeB. Print the percentage of typeA and typeB pixels in your chosen image.

"""

threshold = (0.71111, 0.71111, 0.711111, 1)
array = numpy.asarray(labrat)

bcount = 0
acount = 0
for rows in array:
    for cols in rows:
        if all(cols > threshold):
            acount = acount + 1
        else:
            bcount = bcount + 1

print("Type B percentage:", bcount * 100 / (bcount + acount))
print("Type A percentage:", acount * 100 / (bcount + acount))

imgplot = plt.imshow(labrat)

plt.show()
