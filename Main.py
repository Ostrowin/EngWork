from PIL import Image, ImageOps

pngfile = Image.open('Img/tab1_black.jpg').convert('L').point(lambda x: 0 if x<128 else 255, '1')

pngfile.show()
