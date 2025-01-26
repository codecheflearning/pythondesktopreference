import cv2

#read image
image=cv2.imread("images\\lion.jpg")
print(f'Image Height ={image.shape[0]}, Image Width ={image.shape[1]}',)

#Resize to 25% keeping the aspect ratio
thumbnail = cv2.resize(image, None, fx = 0.25, fy = 0.25)

cv2.imwrite("images\\lion_thumb_cv2.jpg", thumbnail)
