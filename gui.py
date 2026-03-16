# BASIC TKINTER GUI WINDOW

# import tkinter as tk

# window = tk.Tk()
# window.title("Face Recognition Attendance System")
# window.geometry("400x350")

# title = tk.Label(window,
#                  text="Face Recognition Attendance",
#                  font=("Arial",16))
# title.pack(pady=20)

# window.mainloop()

#EXPLAIN THIS ABOVE CODE
# The above code creates a basic GUI window using the Tkinter library in Python. Here's a breakdown of what each part does:
# 1. `import tkinter as tk`: This line imports the Tkinter library and gives it the alias 'tk' for easier reference.
# 2. `window = tk.Tk()`: This line creates a new Tkinter window object and assigns it to the variable 'window'.
# 3. `window.title("Face Recognition Attendance System")`: This line sets the title of the window to "Face Recognition Attendance System".  
# 4. `window.geometry("400x350")`: This line sets the size of the window to 400 pixels wide and 350 pixels tall.
# 5. `title = tk.Label(window, text="Face Recognition Attendance", font=("Arial",16))`: This line creates a label widget with the text "Face Recognition Attendance" and sets the font to Arial with a size of 16. The label is associated with the 'window' as its parent.
# 6. `title.pack(pady=20)`: This line adds the label to the window and applies padding of 20 pixels on the y-axis to create space around the label.
# 7. `window.mainloop()`: This line starts the Tkinter event loop, which keeps the window open and responsive to user interactions until it is closed.

import tkinter as tk
import os
from tkinter import messagebox

def start_attendance():
    os.system("python main.py")

def add_student():
    from tkinter import messagebox

def add_student():

    top = tk.Toplevel(window)
    top.title("Add Student")
    top.geometry("300x200")

    label = tk.Label(top, text="Enter Student Name")
    label.pack(pady=10)

    name_entry = tk.Entry(top)
    name_entry.pack(pady=10)

    def submit_name():

        name = name_entry.get().strip()

        base_folder = r"C:\Users\harsh sirohi\OneDrive\Desktop\Python\project\pictures"
        person_folder = os.path.join(base_folder, name)

        # 1️⃣ Name cannot be empty
        if name == "":
            messagebox.showerror("Error", "Name cannot be empty")
            return

        # 2️⃣ Student already exists
        if os.path.exists(person_folder):
            messagebox.showwarning("Warning", "Student already exists")
            return

        # Start capture
        os.system(f"python capture_pics.py {name}")
        top.destroy()

    submit_btn = tk.Button(top, text="Start Capture", command=submit_name)
    submit_btn.pack(pady=10)

def view_attendance():
    os.startfile("attendance.csv")

window = tk.Tk()
window.title(" ")
window.geometry("500x350")

title = tk.Label(window,text="Welcome To Face Recognition Attendance System",font=("Arial",16))
title.pack(pady=20)

btn1 = tk.Button(window,text="Start Attendance",width=20,command=start_attendance)
btn1.pack(pady=10)

btn2 = tk.Button(window,text="Add Student",width=20,command=add_student)
btn2.pack(pady=10)

btn3 = tk.Button(window,text="View Attendance",width=20,command=view_attendance)
btn3.pack(pady=10)

btn4 = tk.Button(window,text="Exit",width=20,command=window.destroy)
btn4.pack(pady=10)

window.mainloop()