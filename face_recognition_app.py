import cv2
import face_recognition
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

known_image = face_recognition.load_image_file("known.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret: break

    rgb = frame[:, :, ::-1]
    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    for face_encoding, (top, right, bottom, left) in zip(encodings, faces):
        match = face_recognition.compare_faces([known_encoding], face_encoding)[0]
        name = "Recognized" if match else "Unknown"

        db.collection("face_logs").add({
            "name": name,
            "time": datetime.utcnow().isoformat()
        })

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()