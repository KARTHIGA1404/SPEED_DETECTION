**Vehicle Speed Detection Using OpenCV**

---

### 🚗 Vehicle Speed Tracking System

This Python project detects moving vehicles in a video and estimates their speed using basic computer vision techniques with OpenCV. It tracks each vehicle across frames and calculates speed based on displacement over time.

---

### 📂 Project Structure

```
vehicle_speed_tracking/
├── vehicle_speed_tracking.py  # Main script
├── video5.mp4                 # Input video file (replace with your own)
└── README.md                  # Project documentation
```

---

### 🔧 Requirements

* Python 3.x
* OpenCV
* NumPy

Install dependencies:

```bash
pip install opencv-python numpy
```

---

### ▶️ How to Run

1. Place your video file in the project directory and rename it to `video5.mp4` or change the path in the script.
2. Run the script:

```bash
python vehicle_speed_tracking.py
```

3. Press `Q` to quit the video window.

---

### ⚙️ How It Works

* Reads frames from the input video.
* Detects motion using frame differencing and contour detection.
* Tracks each detected vehicle by matching position across frames.
* Calculates speed = distance / time using frame rate and pixel displacement.
* Annotates each vehicle with ID and estimated speed in meters per second.

---

### 🧠 Key Features

* Motion detection using background subtraction (frame differencing).
* Speed estimation based on pixel movement and video FPS.
* Unique ID tracking of each vehicle.
* Adjustable parameters for scale factor and detection sensitivity.

---

### 📌 Parameters

* `scale_factor`: Converts pixel distance to real-world distance (meters).
* `fps`: Frames per second extracted from the video.
* `cv2.contourArea > 500`: Ignores small movements/noise.
* Matching threshold: 50 pixels for tracking continuity.

---

### 📈 Output

* Annotated video frame with:

  * Bounding box around moving vehicle
  * Vehicle ID
  * Estimated speed (m/s)

---
## 📸 Output Frame Example

![s1](https://github.com/user-attachments/assets/71a66cf7-708c-486e-b777-e7485d1071ad)
![s3](https://github.com/user-attachments/assets/53062cab-e7c3-47d7-951f-5059d65792e1)
![s2](https://github.com/user-attachments/assets/c121840c-c166-4a3b-8fd6-eec7ce820892)

---
### 📌
### The above speed detection is one part of this comprehensive project. 
The Accident Detection and Alert System is a real-time AI-powered solution that identifies road accidents, detects overspeeding vehicles, and recognizes victims using facial recognition technology. By analyzing live or recorded CCTV footage with computer vision models, the system detects incidents instantly and sends alert messages containing the date, time, and exact location to the nearest police station or emergency contact. It maintains privacy by not storing any personal data and dynamically manages traffic flow during emergencies by counting vehicles in all directions and adjusting traffic signals accordingly. This intelligent system enhances road safety, accelerates emergency response, and supports effective traffic management. 












