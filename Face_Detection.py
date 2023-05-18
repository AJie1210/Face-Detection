import cv2

video  = cv2.VideoCapture(1)

while True:
    bol, frame = video.read() # bol：是否成功讀取影像 frame：讀取到的影像
    if bol:
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5) # 重新縮放影像大小
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 將影像由BGR轉為灰階
        face = cv2.CascadeClassifier('face_detected.xml') # 導入臉部偵測模型
        faceRect = face.detectMultiScale(gray, 1.1, 7) # 開始進行臉部偵測（偵測圖片、縮小倍數、最低臉部偵測數量）
        print(faceRect)
        print(len(faceRect))

        for(x, y, w, h) in faceRect: # 臉部匡選
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  
            cv2.imshow('display video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('s'):
        break