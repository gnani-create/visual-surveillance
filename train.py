from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Set window size
        self.root.title("Face Recognition System to Identify the Criminals")

        # Title Label
        title_lbl = Label(self.root, text="Train Data Set", font=("Times New Roman", 40, "bold"), bg="yellow", fg="black")
        title_lbl.place(x=-100, y=0, width=1530, height=38)

        # Load and resize the image
        img_top = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\img.jpg")
        img_top = img_top.resize((1250, 250), Image.Resampling.LANCZOS)  # Resize the image to fit the window width
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        # Create a label to display the image
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=-130, y=40, width=1530, height=200)  # Adjusted the y position and height for better display
        
        # Train Data Button
        b1_1 = Button(self.root, text="TRAIN DATA", cursor="hand2", font=("times new roman", 30, "bold"), fg="white", bg="black", command=self.train_classifier)
        b1_1.place(x=0, y=245, width=1270, height=60)

    def train_classifier(self):
        print("Training started...")  # Debugging: Check if the function is triggered
        data_dir = r"D:\python\data"  # Use the correct path for your data

        # Check if directory exists
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"The directory {data_dir} does not exist!")
            return

        images = []  # To store image data
        ids = []  # To store corresponding IDs

        # Loop through all files in the directory
        for file in os.listdir(data_dir):
            if file.endswith(".jpg") or file.endswith(".png"):
                image_path = os.path.join(data_dir, file)
                img = Image.open(image_path).convert('L')  # Convert image to grayscale
                imageNp = np.array(img, 'uint8')

                # Extract user ID from the filename (e.g., 'user.2.1.jpg' → ID 2)
                try:
                    id = int(file.split('.')[1])  # Extract the ID from the filename
                    images.append(imageNp)
                    ids.append(id)
                    print(f"Processed image: {file}, ID: {id}")  # Debugging: Check which files are being processed
                except Exception as e:
                    print(f"Error processing {file}: {e}")  # Error handling for malformed filenames

        if len(images) == 0:
            messagebox.showerror("Error", "No valid images found in the directory!")
            return

        ids = np.array(ids)

        try:
            # Train the classifier using LBPH (Local Binary Pattern Histogram)
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(images, ids)
            clf.write("classifier.xml")  # Save the classifier to a file
            print("Training completed and saved.")  # Debugging: Check if training completed
            messagebox.showinfo("Result", "Training datasets completed")
        except Exception as e:
            print(f"Error during training: {e}")  # Handle any errors during the training process

# Run the application
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
