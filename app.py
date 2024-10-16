import cv2

img = cv2.imread('photo.jpg')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

if len(faces) == 0:
    print("Лица не найдены.")
else:
    print(f"Найдено {len(faces)} лицо(а):")
    for (x, y, w, h) in faces:
        print(f"Координаты: x={x}, y={y}, ширина={w}, высота={h}")
