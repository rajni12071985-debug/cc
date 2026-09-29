import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image



fname = 'bird.jpg'

# opening image using pil

image = Image.open(fname).convert('L')

# mapping image to gray scale 

plt.imshow(image , cmap = 'gist_heat_r')

plt.grid()

plt.show()