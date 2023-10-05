import cv2

image = cv2.imread('pic\\pic1.jpg')

image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('Display picture', image)
img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# 偵測特徵檔路徑:
faceDetected = cv2.CascadeClassifier('face_detected.xml')
# 偵測物件方法:
# detectMultiScale(#圖片-image, #偵測原理-scaleFactor = 1.1, #誤檢率參數-minNeighbors = 3, #最小偵測區塊-minSize = (10, 10), #檢測模式-flags = cv2.CASCADE_SCALE_IMAGE) 
face = faceDetected.detectMultiScale(img, 1.1, 3)

#框選臉部
count = 1
for(x, y, w, h) in face:
    cv2.rectangle(image, (x, y), (x+w, y+h),(0, 0 , 255), 2)
    #擷取臉部
    filename = "pic_copy\\image_" + str(count) + ".jpg"
    image1 = image[y: y + h, x: x + w]
    image1 = cv2.resize(image1, (400, 400))
    cv2.imwrite(filename, image1)
    count = count + 1
cv2.waitKey(2000)