import cv2

# Load Haar Cascade Face Detection Model
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Start Webcam
camera = cv2.VideoCapture(0)

print("=" * 45)
print("      Smart face detection activated      ")
print("         Press Q to close the smart Face detection             ")
print("=" * 45)

while True:

    # Read frame from webcam
    ret, frame = camera.read()

    # If camera not working
    if not ret:
        print("Unable to access camera")
        break

    # Convert image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangle around face
    for (x, y, w, h) in faces:

        # Face rectangle
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # AI Label
        cv2.putText(
           frame,
            "Human Face",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    # Display number of faces detected
    cv2.putText(
        frame,
        f"Faces Detected: {len(faces)}",
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Show webcam window
    cv2.putText(
    frame,
    "Created by Shalini",
    (10, 80),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (255, 255, 255),
    2
)
    cv2.imshow("Face Detection AI", frame)

    # Press Q to Exit
    if cv2.waitKey(10) == ord("q"):
        break

# Release webcam and close windows
camera.release()
cv2.destroyAllWindows()