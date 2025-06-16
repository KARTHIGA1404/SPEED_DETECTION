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

![Detected Vehicle](C:\Users\karth\Downloads\SPEED_DETECTION-main\SPEED_DETECTION-main\images\s1.png)
![Detected Vehicle](images/s2.png)
![Detected Vehicle](images/s3.png)

---

### 🚀 Future Improvements

* Use object detection (YOLO, SSD) for better accuracy.
* Implement Kalman Filter or SORT for robust tracking.
* Add speed threshold alerts (overspeed detection).
* Convert speed to km/h.

---


