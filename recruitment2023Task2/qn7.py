import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy
import math

img = "ddd.png"

# RGB(3 streams) matrix representation of the image
image = mpimg.imread(img)
print(image)

"""

Write the script wrt the given instruction here.

Define a threshold or a limit, (for example (160,160,160)) and if the RGB values of a pixel at a certain position in your chosen image is all greater than the threshold, then consider it to be typeA, else typeB. Print the percentage of typeA and typeB pixels in your chosen image.

"""

threshold = 0.25
height, width, _ = image.shape
bw_image = numpy.zeros((height, width))
for i in range(height):
    for j in range(width):
        brightness = (
            0.21 * image[i, j, 0] + 0.72 * image[i, j, 1] + 0.07 * image[i, j, 2]
        ) / 3
        print("Brightness: ", brightness)
        print("Threshold: ", threshold)
        if brightness > threshold:
            bw_image[i, j] = 0
        else:
            bw_image[i, j] = 1


imgplot = plt.imshow(bw_image, cmap="Greys_r")

plt.show()
