import cv2
import mediapipe as mp
import time
import serial
import math

# === CONFIG ===
PORT = "/dev/tty.usbserial-0001"  # your ESP32 port
BAUD = 115200
esp = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)
print("✅ Connected to ESP32 via Serial")

# === Mediapipe setup ===
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True)
mp_drawing = mp.solutions.drawing_utils

# === Helper: Eye aspect ratio ===
def eye_aspect_ratio(landmarks, eye_indices, w, h):
    pts = [(int(landmarks[i].x * w), int(landmarks[i].y * h)) for i in eye_indices]
    A = math.dist(pts[1], pts[5])
    B = math.dist(pts[2], pts[4])
    C = math.dist(pts[0], pts[3])
    ear = (A + B) / (2.0 * C)
    return ear

# === Indices for eyes (from mediapipe face mesh) ===
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

cap = cv2.VideoCapture(0)
prev_state = "NEUTRAL"
cooldown = 0
last_state_change = time.time()

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("⚠️ No webcam frame.")
        break

    h, w, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            ear_left = eye_aspect_ratio(face_landmarks.landmark, LEFT_EYE, w, h)
            ear_right = eye_aspect_ratio(face_landmarks.landmark, RIGHT_EYE, w, h)
            ear = (ear_left + ear_right) / 2.0

            # Decision logic
            if ear > 0.23:
                state = "FOCUS"
            else:
                state = "RELAX"

            # Cooldown logic to avoid spamming ESP
            if state != prev_state and (time.time() - last_state_change) > 1.5:
                esp.write((state + "\n").encode())
                print(f"🧠 Sent to ESP32 → {state}  (EAR={ear:.2f})")
                last_state_change = time.time()
                prev_state = state

            # Visual feedback
            color = (0, 255, 0) if state == "FOCUS" else (0, 0, 255)
            cv2.putText(frame, f"STATE: {state}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
            mp_drawing.draw_landmarks(
                frame,
                face_landmarks,
                mp_face_mesh.FACEMESH_TESSELATION,
                mp_drawing.DrawingSpec(color=(100, 255, 100), thickness=1, circle_radius=1)
            )

    cv2.imshow("🧠 NeuroIoT Eye-Tracking Focus Detector", frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break  # press ESC to quit

cap.release()
esp.close()
cv2.destroyAllWindows()
