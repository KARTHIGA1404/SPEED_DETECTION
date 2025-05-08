import cv2
import numpy as np

def main():
    video_path = "video5.mp4"  # Replace with your video file path
    video_capture = cv2.VideoCapture(video_path)

    if not video_capture.isOpened():
        print(f"Error: Could not open video file '{video_path}'.")
        return

    prev_frame = None
    cv2.namedWindow("Vehicle Speed Tracking", cv2.WINDOW_NORMAL)

    scale_factor = 0.05  # Conversion factor from pixels to meters
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    frame_interval = 1 / fps
    tracked_vehicles = {}

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Resize frame for better processing
        frame = cv2.resize(frame, (1020, 500))

        # Convert the frame to grayscale and apply Gaussian blur
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)

        if prev_frame is not None:
            # Frame difference and thresholding
            frame_delta = cv2.absdiff(prev_frame, gray)
            thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)

            # Find contours of moving vehicles
            contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            new_tracked_vehicles = {}

            for contour in contours:
                if cv2.contourArea(contour) < 500:  # Only consider large enough contours (vehicles)
                    continue

                # Get bounding box for the contour
                x, y, w, h = cv2.boundingRect(contour)
                center = (x + w // 2, y + h // 2)
                vehicle_id = match_vehicle(center, tracked_vehicles)
                new_tracked_vehicles[vehicle_id] = {'center': center, 'bbox': (x, y, w, h)}

                # Calculate speed if the vehicle was previously tracked
                if vehicle_id in tracked_vehicles:
                    prev_center = tracked_vehicles[vehicle_id]['center']
                    distance = np.linalg.norm(np.array(center) - np.array(prev_center)) * scale_factor
                    speed = distance / frame_interval  # Speed in meters per second
                    new_tracked_vehicles[vehicle_id]['speed'] = speed

                    # Display the speed on the frame
                    cv2.putText(frame, f"ID:{vehicle_id} Speed:{speed:.2f} m/s", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

                # Draw bounding box
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            tracked_vehicles = new_tracked_vehicles

        # Display the frame
        cv2.imshow("Vehicle Speed Tracking", frame)

        # Set the current frame as previous frame for the next iteration
        prev_frame = gray

        # Add delay for slower playback (100 ms)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

def match_vehicle(center, tracked_vehicles):
    """
    Matches the current vehicle to an existing tracked vehicle based on proximity.
    """
    for vehicle_id, data in tracked_vehicles.items():
        prev_center = data['center']
        if np.linalg.norm(np.array(center) - np.array(prev_center)) < 50:  # Threshold for matching
            return vehicle_id
    return len(tracked_vehicles) + 1  # Assign new ID if no match is found

if __name__ == "__main__":
    main()
