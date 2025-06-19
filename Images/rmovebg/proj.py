from rembg import remove
from PIL import Image

image_path = "dilshad.jpg"
result_path = "result.png"

input = Image.open(image_path)
output = remove(input)
output.save(result_path)

