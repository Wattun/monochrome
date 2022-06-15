from PIL import Image
import numpy as np

im = np.array(Image.open('fig/silhouette.jpg'))

print(type(im))

print(im.dtype)

print(im.shape)
