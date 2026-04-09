import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mping
img=mping .imread('image.png')
print("Shape: ",img.shape,"\nDimension: ",img.ndim,"\nData type: ",img.dtype)
canvas=np.zeros_like(img)
crop=img[100:500,200:600]
red=img[:,:,0]
red_image=np.zeros_like(img)
red_image[:,:,0]=red
background=mping.imread('image1.png')
background=background[:img.shape[0],:img.shape[1]]
green=img[:,:,1]>150
green_screen=img.copy()
green_screen[green]=background[green]
bright_img=img+50
bright_img=np.clip(bright_img,0,255)
gamma=1.5
gamma_corrected=np.power(img/255.0,gamma)*255
vintage=np.sqrt(img/255.0)*255
print("Bringhtest pixel: ",np.max(img),"\nDarkest pixal: ",np.min(img),"\nAverage : ",np.mean(img))
plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
plt.title("Original")
plt.imshow(img)
plt.axis("off")
plt.subplot(2, 3, 2)
plt.title("Cropped")
plt.imshow(crop)
plt.axis("off")
plt.subplot(2, 3, 3)
plt.title("Red Channel")
plt.imshow(red_image)
plt.axis("off")
plt.subplot(2, 3, 4)
plt.title("Green Screen")
plt.imshow(green_screen)
plt.axis("off")
plt.subplot(2, 3, 5)
plt.title("Brightened")
plt.imshow(bright_img.astype(np.uint8))
plt.axis("off")
plt.subplot(2, 3, 6)
plt.title("Vintage Filter")
plt.imshow(vintage.astype(np.uint8))
plt.axis("off")
plt.tight_layout()
plt.show()