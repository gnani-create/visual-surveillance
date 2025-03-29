from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from criminal import criminal  # Import the criminal window
from train import Train
from face_recognition import Face_recognition
from criminalidentified import CriminalIdentified


class face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Set window size
        self.root.title("Face Recognition System to Identify the Criminals")

        # First Image
        img = Image.open(r"C:\Users\GNANESHWAR\Desktop\face\2d1d844d-19de-41a4-bb14-c30434411a33.jpeg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=100)

        # Second Image
        img = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\26e7ebce-41b5-4ad4-9647-66f6d57fe976.jpeg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img)
        f_lbl2 = Label(self.root, image=self.photoimg1)
        f_lbl2.place(x=500, y=0, width=400, height=100)

        # Third Image
        img = Image.open(r"C:\Users\GNANESHWAR\Desktop\face\2d1d844d-19de-41a4-bb14-c30434411a33.jpeg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img)
        f_lbl3 = Label(self.root, image=self.photoimg2)
        f_lbl3.place(x=900, y=0, width=500, height=100)

        # Background Image
        img_bg = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\0609524d-6c28-47fb-9308-9d85381ab023.jpeg")
        img_bg = img_bg.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img_bg)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1400, height=600)

        # Title Label
        title_lbl = Label(bg_img, text="Face Recognition System to Identify the Criminals", font=("Times New Roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1500, height=50)

        # Criminal Button
        img_criminal = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\save.jpeg")
        img_criminal = img_criminal.resize((100, 200), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img_criminal)
        b1 = Button(bg_img, image=self.photoimg4, command=self.criminal_details, cursor="hand2")
        b1.place(x=50, y=170, width=100, height=150)

        # Criminal Details Button
        b1_1 = Button(bg_img, text="Criminal Details", command=self.criminal_details, cursor="hand2", font=("Times New Roman", 10, "bold"), bg="red", fg="white")
        b1_1.place(x=50, y=320, width=100, height=20)

        # Detect Face Button
        img_criminal1 = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\crime.jpeg")
        img_criminal1 = img_criminal1.resize((100, 200), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img_criminal1)
        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b2.place(x=300, y=170, width=100, height=150)

        # Face Detector Button
        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("Times New Roman", 12, "bold"), bg="red", fg="white")
        b2_1.place(x=300, y=320, width=100, height=20)

        # Train Data Button
        img_train = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\train2.jpeg")
        img_train = img_train.resize((100, 200), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img_train)
        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.train_data)
        b3.place(x=550, y=170, width=100, height=150)

        # Train Data Button
        b3_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data,font=("Times New Roman", 13, "bold"), bg="red", fg="white")
        b3_1.place(x=550, y=320, width=100, height=20)


        # Last Visited Button
        img_lastvisited = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\lastvisited.jpeg")
        img_lastvisited = img_lastvisited.resize((100, 200), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img_lastvisited)
        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.last_visited_data,)
        b6.place(x=800, y=170, width=100, height=150)

        # Last Visited Button Label
        b6_1 = Button(bg_img, text="Last Visited", cursor="hand2", command=self.last_visited_data,font=("times new roman", 12, "bold"), bg="red", fg="white")
        b6_1.place(x=800, y=320, width=100, height=20)

        # Photos Button
        img_photos = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\photos.jpeg")
        img_photos = img_photos.resize((100, 200), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img_photos)
        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.open_img)
        b7.place(x=1050, y=170, width=100, height=150)

        # Photos Button Label
        b7_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("Times New Roman", 15, "bold"), bg="red", fg="white")
        b7_1.place(x=1050, y=320, width=100, height=20)

    def open_img(self):
        os.startfile("data")

    def criminal_details(self):
        self.new_window = Toplevel(self.root)
        self.app = criminal(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognition(self.new_window)

    def last_visited_data(self):
        self.new_window = Toplevel(self.root)
        self.app = CriminalIdentified(self.new_window)



# Run the application
if __name__ == "__main__":
    root = Tk()
    obj = face_recognition_system(root)
    root.mainloop()
