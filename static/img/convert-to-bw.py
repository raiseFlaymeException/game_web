from PIL import Image
import sys

if len(sys.argv) == 1:
    name = input("Enter the img name: ")
else:
    name = sys.argv[1]
try:
    extension_index = len(name) - name[::-1].index(".")
    extension = "."+name[extension_index:]
    name = name[:extension_index-1]
except ValueError:
    print("You forgot the extension")
    exit(-1)

img = Image.open(name+extension)

width, height = img.size

for x in range(width):
    for y in range(height):
        r, g, b, a = img.getpixel((x, y))
        img.putpixel((x, y), (int((r+g+b)/3), int((r+g+b)/3), int((r+g+b)/3), a))

img.save(name+"-bw"+extension)