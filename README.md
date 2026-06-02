# 😊 Emotion Detection Program

An AI-powered Emotion Detection System that uses Deep Learning and Computer Vision to recognize human emotions from facial expressions in real-time using a webcam.

## 📌 Overview

This project detects facial emotions from live video input. The system identifies faces, processes facial features, and predicts the emotional state of a person using a Convolutional Neural Network (CNN) model trained on facial expression datasets. Emotion recognition is a popular application of Artificial Intelligence in healthcare, education, security, and human-computer interaction. :contentReference[oaicite:0]{index=0}

## 🎯 Features

- Real-time emotion detection using webcam
- Face detection using OpenCV
- Deep Learning-based emotion classification
- User-friendly interface
- Fast and accurate predictions
- Supports multiple emotion categories

## 😊 Detected Emotions

The model can recognize the following emotions:

- Angry 😠
- Disgust 😖
- Fear 😨
- Happy 😄
- Sad 😢
- Surprise 😲
- Neutral 😐

These are common emotion classes used in facial expression recognition datasets. :contentReference[oaicite:1]{index=1}

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Matplotlib

## 📂 Project Structure

```text
emotion_dection_program/
│
├── dataset/
├── model/
├── train_model.py
├── model_video.py
├── requirements.txt
├── README.md
└── other project files
