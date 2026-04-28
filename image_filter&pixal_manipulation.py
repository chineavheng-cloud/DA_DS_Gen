import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('image1.jpg')
print(f"img: {img}")

print(f"img.shape: {img.shape}")
print(f"img.ndim: {img.ndim}")
print(f"img.dtype: {img.dtype}")
print(f"type(img): {type(img)}")
print(f"img.size: {img.size}") # 43074084

blank_canvas = np.zeros((3148, 4561, 3), dtype='uint8')
print(f"blank_canvas : {blank_canvas}")
print(f"blank_canvas.shape : {blank_canvas.shape}")

plt.imshow(img)
plt.axis('off')
plt.show()

imgv2 = img.copy()

# slicing

imgv2 = imgv2[100:500, 200:600]

# plt.imshow(img)
# plt.axis('off')
# plt.show()

# plt.imshow(imgv2)
# plt.axis('off')
# plt.show()

# indexing
imgv2_red_only = imgv2.copy()

# print(f"imgv2_red_only before isolate: {imgv2_red_only}")

# # isolate red only
# [red, green, blue] <=> '0 for red', '1 for green', '2 for blue'
imgv2_red_only[:, :, 1] = 0
imgv2_red_only[:, :, 2] = 0

# print(f"imgv2_red_only after isolate: {imgv2_red_only}")

# plt.imshow(imgv2_red_only)
# plt.axis('off')
# plt.show()

# masking

imgv2_green_only = imgv2.copy()

# creating the mask (green > 200)
masking_screen = imgv2_green_only[:, :, 1] > 200
masking_screen_value = imgv2_green_only[masking_screen]
random_cropped_green_imgv2 = np.random.randint(0, 256, size=(len(masking_screen_value)), dtype='uint8')

imgv2_green_only[masking_screen, 1] = random_cropped_green_imgv2

# print(f"len of the masking_screen is: {len(masking_screen)}")
# print(f"len of the masking_screen_value is: {len(masking_screen_value)}")

# print(f"masking_screen: {masking_screen}")
# print(f"masking_screen_value: {masking_screen_value}")

# plt.imshow(imgv2)
# plt.axis('off')
# plt.show()

# plt.imshow(imgv2_green_only)
# plt.axis('off')
# plt.show()

