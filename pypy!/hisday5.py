import cv2

# تهيئة مُكون كشف الوجه
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# تهيئة الكاميرا الأولى
current_camera_index = 1
cap = cv2.VideoCapture(current_camera_index)

while True:
    # قراءة الإطار الحالي من الكاميرا
    ret, frame = cap.read()

    # تحويل الإطار إلى اللون الرمادي
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # كشف الوجوه في الإطار الرمادي
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # رسم مربع حول الوجوه المكتشفة
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # عرض الإطار المعالج
    cv2.imshow('Face Detection', frame)

    # الانتظار للضغط على مفتاح 'c' لتغيير الكاميرا
    key = cv2.waitKey(1)
    if key == 27:  # رمز ESC هو 27
        break
    elif key == ord('c'):
        # تبديل بين الكاميرات
        cap.release()
        current_camera_index = 1 - current_camera_index  # Switch between 0 and 1
        cap = cv2.VideoCapture(current_camera_index)

# إغلاق الكاميرا
cap.release()

# تدمير النوافذ
cv2.destroyAllWindows()
