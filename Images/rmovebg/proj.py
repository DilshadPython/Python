from PIL import Image
from rembg import remove

# image_path = "dilshad.jpg"
# result_path = "result.png"

image_path = "ario.jpg"
result_path = "ario_after.png"

input = Image.open(image_path)
output = remove(input)
output.save(result_path)
