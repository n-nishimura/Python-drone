import cv2 as cv
# opencvと顔認識の準備
# Classifierというメソッドにxmlファイルを読み込む
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

img = cv.imread('photo-py.jpeg')

# grayイメージを作る
gray = cv.cvtColor(img,cv.COLOR_BG2GRAY)
faces = face_cascade.detectMultiScale(gray , 1.3 , 5)

print(len(faces))
# faceとして認識されたものがいくつあるか

# 顔を四角で囲む
for (x , y , w , h) in faces:
  cv.rectangle (img ,(x,y) , (x+w, y+h),(255,0,0),2)


