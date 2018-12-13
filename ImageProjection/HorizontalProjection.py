from pylab import *
from PIL import Image
class HorizontalProjection:
    
    def __init__(self, image):
        self.image = image
        self.data = array(self.image)
        #self.red, self.green, self.blue = self.data.T
        self.width, self.height = self.image.size
        
    def axesY(self):
        plot([1,2,3,4])
        savefig('wykres.png')
        
    def printImage(self):
        self.image.show()
        
    def printData(self):
        print(self.width)
        print(self.height)
        print(self.data)

    def getProjection1(self):
        numberOfOnes = 0
        dataPlot = []
        for(i,row)in enumerate(self.data):
            for(j,value) in enumerate(row):
                if self.data[i][j]:
                    numberOfOnes += 1
            dataPlot.append(numberOfOnes)
            numberOfOnes = 0

        plot(dataPlot)
        savefig('wykres.png')

    def getProjection2(self):
        dataPlot = [0] * shape(self.data)[1]
        for(i,row)in enumerate(self.data):
            for(j,value) in enumerate(row):
                if self.data[i][j]:
                    dataPlot[j] += 1

        plot(dataPlot)
        savefig('wykres2.png')
