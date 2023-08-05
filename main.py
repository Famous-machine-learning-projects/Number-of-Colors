import cv2

image = cv2.imread('sunset.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width, _ = image_rgb.shape

unique_colors = set()
for y in range(height):
    for x in range(width):
        pixel_color = tuple(image_rgb[y, x])
        unique_colors.add(pixel_color)

print(len(unique_colors))
