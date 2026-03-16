# face-recognition-attendance-system
A Python-based Face Recognition Attendance System using OpenCV and face_recognition library that automatically marks attendance and prevents duplicate entries within 24 hours.
## Overview
The **Face Recognition Attendance System** is a Python-based application that automatically marks attendance by recognizing faces through a webcam.
It uses computer vision and machine learning to detect and recognize faces in real time and records attendance in a CSV file.

---

## Features

* Real-time face detection using OpenCV
* Face recognition using the `face_recognition` library
* Automatic attendance marking
* Prevents duplicate attendance within 24 hours
* Simple GUI interface using Tkinter
* Stores attendance records in a CSV file

---

## Technologies Used

* Python
* OpenCV
* face_recognition
* NumPy
* Tkinter
* pyttsx3 (Text-to-Speech)

---

## Project Structure

```
face-recognition-attendance-system
│
├── main.py
├── gui.py
├── capture_pics.py
├── requirements.txt
├── attendance.csv
├── .gitignore
└── README.md
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/harshsirohi-dev/face-recognition-attendance-system.git
```

### 2️. Navigate to the project directory

```
cd face-recognition-attendance-system
```

### 3️. Install dependencies

```
pip install -r requirements.txt
```

---

## 4. Running the Project

Run the main program:

```
python main.py
```

The webcam will start and the system will detect and recognize faces automatically.

---

##  Attendance Storage

Attendance is recorded in a **CSV file** with:

* Name
* Date
* Time

Duplicate attendance entries for the same person within the same day are prevented.

---

## Future Improvements

* Database integration (MySQL / PostgreSQL)
* Web dashboard for attendance reports
* Cloud deployment
* Mobile integration

---

## Author

**Harsh Sirohi**

GitHub:
https://github.com/harshsirohi-dev

---
