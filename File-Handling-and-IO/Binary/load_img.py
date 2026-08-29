import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    #adding all image to one list of images
    images.append(image)

# loop=0 this is means infinitive loop, duration speed of 100
images[0].save(
    'pictures.gif', save_all=True, append_images=[images[1]], duration=100, loop=0,
)


