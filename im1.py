
from PIL import Image
m=Image.open('zzz.jpg')
m.convert(mode='L').save('z2.png')