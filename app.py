import cv2

# Загрузка изображения из текущей директории
img = cv2.imread('755163518648594.jpg')

# Загрузка классификатора для поиска лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Преобразуем изображение в градации серого
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Поиск лиц на изображении
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Вывод координат найденных лиц
if len(faces) == 0:
    print("Лица не найдены.")
else:
    print(f"Найдено {len(faces)} лицо(а):")
    for (x, y, w, h) in faces:
        print(f"Координаты: x={x}, y={y}, ширина={w}, высота={h}")
