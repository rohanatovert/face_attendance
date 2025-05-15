

# Facial Attendance System 

## Overview
This repository contains a **Facial Attendance System** built using **Streamlit** for the UI and **face_recognition** for detecting and recognizing faces. The system captures live video, identifies individuals using stored images, and logs their attendance.

## Dependencies
Ensure you have the following libraries installed before running the application:

```bash
pip install streamlit opencv-python numpy face_recognition pandas
```

Additionally, ensure that the `haarcascade_frontalface_default.xml` file is available for face detection.

## Project Structure
The key components of the project are:

- `app.py` – The main Streamlit application that handles UI interactions.
- `Facial_2.py` – Handles face detection, recognition, and attendance logging.
- `Images_2` – Directory containing stored images for face recognition.
- `haarcascade_frontalface_default.xml` – Haarcascade model for face detection.

## Application Workflow
1. **Launch the Streamlit app** by running:
   ```bash
   streamlit run app.py
   ```
2. **User Interface**
   - A **title** is displayed: "Facial Attendance".
   - The UI is divided into two sections: **Video Feed** and **Alerts**.
   - A **Start button** initiates facial recognition.

3. **Face Recognition Process**
   - When the **Start button** is clicked:
     - Live video is displayed.
     - Faces are detected using `haarcascade_frontalface_default.xml`.
     - Recognized faces are matched with stored images in `Images_2`.
     - Attendance is logged with timestamps in a CSV file.

## Attendance Logging
Once a face is recognized:
- The person's details are logged in a **CSV file** with a timestamp.
- A sound alert (`winsound`) notifies successful recognition.

## Future Enhancements
- Integrate **database storage** for attendance records.
- Allow **real-time notifications** for unauthorized users.
- Improve accuracy using **deep learning models**.


