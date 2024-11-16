from PIL import Image
from PIL import ImageChops

img1, img2 = Image.open('1.jpg'), Image.open('2,jpg')
diff = ImageChops.difference(img1, img2)

if diff.getbbox():
    diff.show()
else:
    print ("No difference")