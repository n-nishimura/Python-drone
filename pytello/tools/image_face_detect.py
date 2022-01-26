
import cv2 as cv
import os

cap = cv.VideoCapture(0)



# opencvと顔認識の準備
# Classifierというメソッドにxmlファイルを読み込む
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
# ビデオで撮ったものをframeへ入れる

while True:
    ret, frame = cap.read()

    path = os.path.dirname(__file__)
    # img = cv.imread(path + "/photo-py.jpeg")

    # grayイメージを作る
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3 , 5)
    print(len(faces))

    # faceとして認識されたものがいくつあるか

    # 顔を四角で囲む
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        eye_gray = gray[y:y+h, x:x+w]
        eye_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(eye_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(eye_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv.imshow('frame', frame)
    # 1msec待ってから次のループ
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cv.destroyAllWindows()
