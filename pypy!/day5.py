import cv2

# تحميل مصنف وجه مسبقاً
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'hand_haar_cascade.xml')

# تهيئة مصدر الفيديو
video_capture = cv2.VideoCapture(1)

while True:
    # قراءة الإطار الحالي من الفيديو
    ret, frame = video_capture.read()

    # تحويل الإطار إلى اللون الرمادي
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # الكشف عن الوجوه في الإطار الرمادي
    faces = face_cascade.detectMultiScale(gray,1.3, 5)

    # رسم مربع حول الوجوه المكتشفة
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # عرض الإطار الناتج
    cv2.imshow('Video', frame)

    # انتظار 1 ملي ثانية والتحقق من الضغط على مفتاح "q" لإيقاف التشغيل
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# إغلاق مصدر الفيديو
video_capture.release()

# إغلاق النوافذ المفتوحة
cv2.destroyAllWindows()