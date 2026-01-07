from PIL import Image
import random

im = Image.open("nostalgic.jpg").convert("RGB")
pix = im.load()
x, y = im.size

coords = [(i, j) for i in range(x) for j in range(y)]

key = 999
random.seed(key)
random.shuffle(coords)

flat_pixels = [pix[i, j] for i, j in coords]

k = 0
for i in range(x):
    for j in range(y):
        pix[i, j] = flat_pixels[k]
        k += 1

im.show()
