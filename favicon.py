from PIL import Image
filename = r'favicon.png'
img = Image.open(filename)
img.save('logo.ico')
