import pytesseract
from PIL import Image

im=Image.open('1.jpg')
#进行置灰处理
im=im.convert('L')
#这个是二值化阈值
threshold=150
table=[]
for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)
#通过表格转换成二进制图片，1的作用是白色，0就是黑色
im=im.point(table,"1")
# im.show()
print(pytesseract.image_to_string(im))