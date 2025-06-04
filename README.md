# Face Recognition with Firebase on GCP (Free Tier)

## Overview

This project uses OpenCV and face_recognition in Python to detect and recognize faces from webcam input, log results to Firebase Firestore, and optionally serve a Flask web dashboard.

## Features

- Face recognition via camera
- Logs to Firebase Firestore
- Flask web dashboard to view logs
- Deployable to Google Cloud Run

## Setup

### 1. Clone the Repo

```bash
git clone https://github.com/yourname/face_recognition_gcp.git
cd face_recognition_gcp
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Add Firebase

- Go to Firebase Console
- Create a project
- Enable Firestore (test mode)
- Generate `serviceAccountKey.json` and place it in the project root
- Replace `known.jpg` with your known face image

### 4. Run Locally

```bash
python face_recognition_app.py
```

### 5. Run Web Dashboard

```bash
python flask_app.py
```

### 6. Deploy to Google Cloud Run

```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/face-app
gcloud run deploy face-app --image gcr.io/YOUR_PROJECT_ID/face-app --platform managed --allow-unauthenticated
```

## Project Structure

```
face_recognition_gcp/
├── face_recognition_app.py
├── flask_app.py
├── templates/
│   └── index.html
├── serviceAccountKey.json (not included)
├── known.jpg (not included)
├── requirements.txt
├── Dockerfile
└── README.md
```
