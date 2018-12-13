from PIL import Image
import numpy
import scipy
from scipy import ndimage
from scipy import signal as sg
from ImageProjection.HorizontalProjection import HorizontalProjection
from EdgeDetection.EdgeDetection import EdgeDetection
#pngfile = Image.open('Img/tab1.jpg').convert('L')#.convert('L').point(lambda x: 0 if x<128 else 255, '1')
#ED = EdgeDetection(pngfile)
#ED.SobelOperator()
#HP = HorizontalProjection(pngfile)
#HP.printImage()
#HP.getProjection2()
#pngfile = numpy.array(pngfile)
#matrix2=sg.convolve(matrix1, G1,"valid")
#print(matrix2)
im = scipy.misc.imread('Img/tab1.jpg')
im = im.astype("int32")
edge_horizont = ndimage.sobel(im, 0)
edge_vertical = ndimage.sobel(im, 1)
magnitude = numpy.hypot(edge_horizont, edge_vertical)
magnitude *= 255.0 / numpy.max(magnitude)
scipy.misc.imwrite('sobel.jpg', magnitude)
