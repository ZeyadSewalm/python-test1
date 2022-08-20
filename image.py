from email.mime import image
from tkinter import END
from PIL import Image
import os
s=(300,300)

for i in os.listdir('.'):
 if i.endswith('jpg'):
     f=Image.open(i)
     i1,i2=os.path.splitext(i)
     f.thumbnail(s)
     f.save(f'300/{i1}_300{i2}')