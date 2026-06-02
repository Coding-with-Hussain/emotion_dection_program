import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load model
model = load_model('model.h5')

# Emotion labels
emotion_labels = [
    'Angry','Disgust','Fear','Happy','Sad','Surprise','Neutral'
]

# Load face detector
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load image
image_path = 'H.png'  # 🔥 change this to your image path
frame = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Loop through faces
for (x,y,w,h) in faces:
    face = gray[y:y+h, x:x+w]
    face = cv2.resize(face, (48,48))
    face = face / 255.0
    face = np.reshape(face, (1,48,48,1))

    prediction = model.predict(face)
    emotion = emotion_labels[np.argmax(prediction)]

    # Draw box + label
    cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
    cv2.putText(frame, emotion, (x,y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                (0,255,0), 2)

# Show result
cv2.imshow('Emotion Detection', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()