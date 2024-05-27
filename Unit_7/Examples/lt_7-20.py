from PIL import Image

img = Image.open("test.png")
img.show()
w, h = img.size
print("图片宽高:{}*{}".format(w, h))
img.thumbnail((w//2, h//2))
print("缩放后图片宽高:{}*{}".format(w//2, h//2))
img.save("缩放.jpg", 'jpeg')