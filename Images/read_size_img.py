from PIL import Image

image = Image.open('land.jpg')
width, height = image.size


print(f'{width} | {height} pixels')
