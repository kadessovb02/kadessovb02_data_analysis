from PIL import Image
import random
xx = []
yy = []
rr = []
bb = []
gg = []
def newImg():
    img = Image.new('RGB', (100, 100))
    for i in range(0, 10):
        x = random.randint(0, 100)
        xx.append(x)
        y = random.randint(0, 100)
        yy.append(y)
        r = random.randint(0, 255)
        rr.append(r)
        g = random.randint(0, 255)
        gg.append(g)
        b = random.randint(0, 255)
        bb.append(b)
        img.putpixel((x, y), (r, g, b))
    min = 5
    indexmin = 0
    for i in range(0, 100):
        for j in range(0, 100):
            for k in range(0, 10):
                t = (xx[k] - i)**2 + (yy[k] - j)**2
                if (t < min):
                    t = min
                    indexmin = k
            img.putpixel((i, j), (rr[indexmin], gg[indexmin], bb[indexmin]))
            
            
            
    return img
visualization = newImg()
visualization.save('ans.png')
visualization.show()