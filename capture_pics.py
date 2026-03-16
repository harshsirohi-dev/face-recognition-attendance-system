import cv2
import os
import face_recognition
import pickle


# Ask for person name
import sys
person_name = sys.argv[1]

# Existing folder (DO NOT CHANGE STRUCTURE)
base_folder = r"C:\Users\harsh sirohi\OneDrive\Desktop\Python\project\pictures"

# Create subfolder inside pictures
person_folder = os.path.join(base_folder, person_name)

os.makedirs(person_folder, exist_ok=True)

print("Images will be saved in:", person_folder)

# Start camera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Improve camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)

count = 0

print("\nControls:")
print("Press 'c' to capture image")
print("Press 'q' to quit\n")

while True:

    success, frame = cap.read()

    if not success:
        print("Camera error")
        break

    # Mirror effect
    frame = cv2.flip(frame, 1)

    # Smooth video noise
    frame = cv2.GaussianBlur(frame, (3,3), 0)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(rgb)

    # Draw rectangle
    for (top, right, bottom, left) in faces:
        cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)

    cv2.imshow("Face Dataset Capture", frame)

    key = cv2.waitKey(1) & 0xFF

    # Capture when 'c' pressed
    if key == ord('c'):

        if len(faces) == 1:

            top, right, bottom, left = faces[0]

            face = frame[top:bottom, left:right]

            face = cv2.resize(face, (256,256))

            img_name = f"img_{count+1}.jpg"

            img_path = os.path.join(person_folder, img_name)

            cv2.imwrite(img_path, face)

            count += 1

            print("Captured:", img_name)

        else:
            print("Ensure exactly one face is visible")

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("\nCapture complete")
print("Total images captured:", count)



encoding_file = "encodings.pickle"

print("Updating encodings...")

new_encodings = []
new_names = []

# Encode newly captured images
for img_name in os.listdir(person_folder):

    img_path = os.path.join(person_folder, img_name)

    img = face_recognition.load_image_file(img_path)

    encodes = face_recognition.face_encodings(img)

    if len(encodes) > 0:
        new_encodings.append(encodes[0])
        new_names.append(person_name)

# Load existing encodings if file exists
if os.path.exists(encoding_file):

    with open(encoding_file, "rb") as f:
        encodeListKnown, classNames = pickle.load(f)

    encodeListKnown.extend(new_encodings)
    classNames.extend(new_names)

else:
    encodeListKnown = new_encodings
    classNames = new_names

# Save updated encodings
with open(encoding_file, "wb") as f:
    pickle.dump((encodeListKnown, classNames), f)

print("Encodings updated successfully.")