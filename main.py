# import cv2
# import face_recognition
# import os


# # -----------STEP 1 - Load the images and find the encodings------------


# path = r"C:\Users\harsh sirohi\OneDrive\Desktop\Python\project\pictures"

# images = []
# classNames = []

# for person in os.listdir(path):

#     person_folder = os.path.join(path, person)

#     for img_name in os.listdir(person_folder):

#         img_path = os.path.join(person_folder, img_name)

#         img = cv2.imread(img_path)

#         images.append(img)
#         classNames.append(person)

# print("Persons in dataset:", set(classNames))

# def findEncodings(images):
#     encodeList = []

#     for img in images:

#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#         encodes = face_recognition.face_encodings(img)

#         if len(encodes) > 0:
#             encodeList.append(encodes[0])

#     print("All encodings completed. Starting face recognition...")

#     return encodeList
# encodeListKnown = findEncodings(images)

# # -----------STEP 2 - Recognize the faces in the webcam feed------------
# import numpy as np


# cap = cv2.VideoCapture(0)

# # Improve camera resolution
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
# while True:

#     success, img = cap.read()

#     # mirror effect (natural camera view)
#     img = cv2.flip(img, 1)

#     # reduce camera noise
#     img = cv2.GaussianBlur(img, (3,3), 0)
#     if not success:
#         break

#     # Resize frame (speed)
#     imgSmall = cv2.resize(img, (0,0), None, 0.5, 0.5)
#     imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

#     facesCurFrame = face_recognition.face_locations(imgSmall)
#     encodesCurFrame = face_recognition.face_encodings(imgSmall, facesCurFrame)

#     for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):

#         faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
#         matchIndex = np.argmin(faceDis)

#         # stricter threshold (important)
#         if faceDis[matchIndex] < 0.50:

#             name = classNames[matchIndex].upper()

#         else:
#             name = "UNKNOWN"

#         y1, x2, y2, x1 = faceLoc
#         y1, x2, y2, x1 = y1*2, x2*2, y2*2, x1*2

#         cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
#         cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)

#         cv2.putText(img,name,(x1+6,y2-6),
#                     cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

#     cv2.imshow("Face Recognition", img)

#     if cv2.waitKey(1) & 0xFF == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()


from copyreg import pickle

import cv2
import numpy as np
import face_recognition
import os
import csv
from datetime import datetime
import time
import pyttsx3
import pickle





# ATTENDANCE_FILE = "attendance.csv"

# def mark_attendance(name):

#     now = datetime.now()
#     date_today = now.strftime("%Y-%m-%d")
#     time_now = now.strftime("%H:%M:%S")

#     # Create file if it does not exist
#     if not os.path.exists(ATTENDANCE_FILE):
#         with open(ATTENDANCE_FILE, "w", newline="") as f:
#             writer = csv.writer(f)
#             writer.writerow(["Date", "Name", "Time"])

#     # Read existing attendance
#     already_marked = False
#     today_header_exists = False

#     with open(ATTENDANCE_FILE, "r") as f:
#         reader = csv.reader(f)

#         for row in reader:
#             if len(row) == 0:
#                 continue

#             # Check if today's header already exists
#             if row[0] == date_today:
#                 today_header_exists = True

#             # Check duplicate entry
#             if len(row) >= 3:
#                 if row[0] == date_today and row[1] == name:
#                     already_marked = True
#                     break

#     # If already marked today -> do nothing
#     if already_marked:
#         print(f"{name} already marked today.")
#         return

#     # Write attendance
#     with open(ATTENDANCE_FILE, "a", newline="") as f:
#         writer = csv.writer(f)

#         # If new day -> write date header
#         if not today_header_exists:
#             writer.writerow([])
#             writer.writerow([date_today])

#         writer.writerow([name, time_now])

#     print(f"Attendance marked for {name}")
marked_names = set()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_once(name, message):

    current_time = time.time()

    if name not in last_spoken or current_time - last_spoken[name] > cooldown:
        speak(message)
        last_spoken[name] = current_time    

last_spoken = {}
cooldown = 3



def mark_attendance(name, filename="attendance.csv"):

    name = name.strip().upper()

    today = datetime.now().strftime("%Y-%m-%d")
    day_name = datetime.now().strftime("%A")
    time_now = datetime.now().strftime("%H:%M:%S")

    header = f"{day_name}, {today}"

    if not os.path.exists(filename):
        open(filename, "w").close()

    with open(filename, "r+") as f:

        lines = f.readlines()

        # Check if name already marked today
        today_section = False

        for line in lines:

            line = line.strip()

            if line == header:
                today_section = True
                continue

            if today_section:

                if line == "":
                    break

                if line.split(",")[0].strip().upper() == name:
                    return "already_marked"

        # If today's header not present, write it
        if header not in "".join(lines):

            if len(lines) > 0:
                f.write("\n")

            f.write(f"\n{header}\n")

        # Write attendance
        f.write(f"{name},{time_now}\n")

        return "marked"

path = r"C:\Users\harsh sirohi\OneDrive\Desktop\Python\project\pictures"

images = []
classNames = []

path = r"C:\Users\harsh sirohi\OneDrive\Desktop\Python\project\pictures"

persons = os.listdir(path)

print("Persons in dataset:", persons)

for person in persons:

    person_path = os.path.join(path, person)

    for img_name in os.listdir(person_path):

        img_path = os.path.join(person_path, img_name)

        img = cv2.imread(img_path)

        if img is not None:
            images.append(img)
            classNames.append(person)    

print("Loading images completed...")

def findEncodings(images):

    encodeList = []

    for img in images:

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        encodes = face_recognition.face_encodings(img)

        if len(encodes) > 0:
            encodeList.append(encodes[0])

    print("All encodings completed. Starting face recognition...")

    return encodeList

encoding_file = "encodings.pickle"

if os.path.exists(encoding_file):

    print("Loading saved encodings...")

    with open(encoding_file, "rb") as f:
        encodeListKnown, classNames = pickle.load(f)

    print("Encodings loaded instantly.")


else:

    print("No saved encodings found. Creating encodings...")

    encodeListKnown = findEncodings(images)

    with open(encoding_file, "wb") as f:
        pickle.dump((encodeListKnown, classNames), f)

    print("Encodings saved for future runs.")


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Camera resolution (smooth performance)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

process_this_frame = True
marked_today = set()
while True:

    success, img = cap.read()

    img = cv2.flip(img, 1)

    if process_this_frame:

        # Resize for faster processing
        small_img = cv2.resize(img, (0,0), None, 0.25, 0.25)

        rgb_small = cv2.cvtColor(small_img, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(rgb_small)

        encodesCurFrame = face_recognition.face_encodings(rgb_small, facesCurFrame)

    process_this_frame = not process_this_frame


    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):

        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)

        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex] and faceDis[matchIndex] < 0.50:

            name = classNames[matchIndex].upper()
        else:
            name="unknown"

        if name !="unknown":

            if name not in marked_names:
 
                result = mark_attendance(name)

                current_time = time.time()
                
                if result == "marked":
                    marked_names.add(name)


                    if name not in last_spoken or current_time - last_spoken[name] > cooldown:
                        speak(f"Thank you {name}, attendance recorded")
                        last_spoken [name]= current_time

                elif result == "already_marked":
                    marked_names.add(name)

                    if name not in last_spoken or current_time - last_spoken[name] > cooldown:
                        speak(f"{name}, attendance already marked")
                        last_spoken[name]= current_time

                    


        top, right, bottom, left = faceLoc

        # scale back up
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(img,(left,top),(right,bottom),(0,255,0),2)

        cv2.rectangle(img,(left,bottom-35),(right,bottom),(0,255,0),cv2.FILLED)

        cv2.putText(img,name,(left+6,bottom-6),
                    cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

    cv2.imshow("Face Recognition", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()