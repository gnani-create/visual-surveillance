from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
import mysql.connector
import cv2
import os


class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Set window size
        self.root.title("Face Recognition System to Identify the Criminals")

        # Title Label
        title_lbl = Label(self.root, text="Face Recognition", font=("Times New Roman", 40, "bold"), bg="black", fg="white")
        title_lbl.place(x=-100, y=0, width=1530, height=57)

        # 1st image (top image)
        img_top1 = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\0609524d-6c28-47fb-9308-9d85381ab023.jpeg")
        img_top1 = img_top1.resize((650, 590), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl1 = Label(self.root, image=self.photoimg_top1)
        f_lbl1.place(x=650, y=59, width=700, height=590)

        # 2nd image (top image)
        img_top2 = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\2b58a8ae-8035-4620-8f44-140201c6272e.jpeg")
        img_top2 = img_top2.resize((700, 590), Image.Resampling.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)

        f_lbl2 = Label(self.root, image=self.photoimg_top2)
        f_lbl2.place(x=0, y=59, width=700, height=590)

        # Button for face recognition
        b1_1 = Button(f_lbl2, text="Face Recognition", cursor="hand2", font=("times new roman", 30, "bold"), fg="white", bg="black", command=self.face_recog)
        b1_1.place(x=0, y=525, width=700, height=60)

    def mark_identifiedcriminal(self, d, n, s, a):
        with open("identify.csv", "a", newline="\n") as f:
            now = datetime.now()
            d1 = now.strftime("%d/%m/%y")
            dtString = now.strftime("%H:%M:%S")
            f.write(f"\n{d},{n},{s},{a},{dtString},{d1},kukatpally")

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="gnani@23wj1a6278", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM criminal WHERE criminal_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(str(item) for item in n) if n else "Unknown"

                my_cursor.execute("SELECT Station FROM criminal WHERE criminal_id=" + str(id))
                s = my_cursor.fetchone()
                s = "+".join(str(item) for item in s) if s else "Unknown"

                my_cursor.execute("SELECT Age FROM criminal WHERE criminal_id=" + str(id))
                a = my_cursor.fetchone()
                a = "+".join(str(item) for item in a) if a else "Unknown"

                my_cursor.execute("SELECT criminal_id FROM criminal WHERE criminal_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(str(item) for item in d) if d else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"iD: {d}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Station: {s}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Age: {a}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_identifiedcriminal(d, n, s, a)
                else:
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()

        if not os.path.exists("classifier.xml"):
            messagebox.showerror("Error", "Classifier file not found!")
            return

        clf.read("classifier.xml")

        try:
            video_cap = cv2.VideoCapture(0)
            if not video_cap.isOpened():
                messagebox.showerror("Error", "Webcam not accessible!")
                return

            while True:
                ret, img = video_cap.read()
                if not ret:
                    break
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome To Face Recognition", img)

                if cv2.waitKey(1) == 13:  # Enter key to exit the loop
                    break
                elif cv2.getWindowProperty("Welcome To Face Recognition", cv2.WND_PROP_VISIBLE) < 1:
                    break

            video_cap.release()
            cv2.destroyAllWindows()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to access webcam: {str(e)}")


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()








