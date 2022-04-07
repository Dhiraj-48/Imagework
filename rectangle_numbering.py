from unicodedata import name
import cv2 as cv
import numpy as np
from PIL import Image,ImageFont,ImageDraw

# img=cv.imread("C:\\Users\\\Hp\\Documents\\opencv\\imagealign.png")


def dis1(a,b,c,d):
    x1,y1=a,b
    x2,y2=c,d
    d1=np.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return d1


def dis2():
    x1,y1=468,169
    x2,y2=563,142
    d2=np.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return d2

def dis3():
    x1,y1=169,435
    x2,y2=285,368
    d3=np.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return d3

def dis4():
    x1,y1=455,416
    x2,y2=509,447
    d4=np.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return d4  


def compare(a,b,c,d):
    dl1=a
    dl2=b
    dl3=c
    dl4=d
    li=[dl1,dl2,dl3,dl4]
    # print(li)
    sli=np.sort(li)
    # print(sli)
    return sli


if __name__=="__main__":
    a=dis1(201,150,263,166)
    b=dis2()
    c=dis3()
    d=dis4()
    print("The distance of line in first rectangle is:",a)
    print("The distance of line in second rectangle is:",b)
    print("The distance of line in third rectangle is:",c)
    print("The distance of line in fourth rectangle is:",d)
    sl=compare(a,b,c,d)
    print(sl)
    img=Image.open("imagealign.png")
    img_edit=ImageDraw.Draw(img)
    for x in sl:
        # if sl[0]:
            img_txt="1"
            img_edit.text((502,544),img_txt,(0,0,0),font=None)

        # if sl[1]:
            img_txt="2"
            img_edit.text((190,247),img_txt,(0,0,0),font=None)

        # elif sl[2]:
            img_txt="3"
            img_edit.text((502,247),img_txt,(0,0,0),font=None)

        # elif sl[3]:
            img_txt="4"
            img_edit.text((190,544),img_txt,(0,0,0),font=None)

        # else:
        #     print("Invalid!")

    img.save("final.png")
    



# d=np.sqrt(((263-201)**2)+((166-150)**2))
# print(d)