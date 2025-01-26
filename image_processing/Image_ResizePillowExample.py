from PIL import Image

image = Image.open('images\\lion.jpg')
#Thumbnail function is better than image.resize()
#Tt preserves the original aspect ratio of the image
image.thumbnail((200, 200))
image.save('images\\lion_thumbnail.jpg')
print(image.size)