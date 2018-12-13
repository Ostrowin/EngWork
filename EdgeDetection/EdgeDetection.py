import numpy 
import scipy
from scipy import ndimage
class EdgeDetection:
    def __init__(self, image):
        self.image = image

    def SobelOperator(self):
        
        dx = ndimage.sobel(self.image, 0)  # horizontal derivative
        dy = ndimage.sobel(self.image, 1)  # vertical derivative
        mag = numpy.hypot(dy,dx)  # magnitude
        mag *= 255.0 / numpy.max(mag)  # normalize (Q&D)
        scipy.misc.imsave('sobel.jpg', mag)
