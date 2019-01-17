from PIL import Image
import os
for value in range(1,476):
    img = Image.open('C:/test1/'+str(value)+'.jpg')
    box1 = (70, 250, 950, 750)
    image1 = img.crop(box1)
    image1.save('C:/test2/'+str(value)+'.jpg')

value=1
img = Image.open('C:/test1/'+str(value)+'.jpg')
print(img.size[0])



