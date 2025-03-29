from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class criminal:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Set window size
        self.root.title("Face Recognition System to Identify the Criminals")

        # ====================== variables ============

        self.var_criminal_id = StringVar()
        self.var_dep = StringVar()
        self.var_DOB = StringVar()
        self.var_Gender = StringVar()
        self.var_name = StringVar()
        self.var_Age = StringVar()
        self.var_station = StringVar()
        self.var_radio1 = StringVar()

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

        img_bg = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\0609524d-6c28-47fb-9308-9d85381ab023.jpeg")
        img_bg = img_bg.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img_bg)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1400, height=600)

        # Title Label
        title_lbl = Label(bg_img, text="Criminal Identification", font=("Times New Roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1300, height=40)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=45, width=1500, height=500)

        # left label frame
        LEFT_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="current details", font=("times new roman", 12, "bold"))
        LEFT_frame.place(x=15, y=10, width=600, height=480)

        img_left = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\crime.jpeg")
        img_left = img_left.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(LEFT_frame, image=self.photoimg_left)
        f_lbl.place(x=15, y=0, width=500, height=100)

        Department_information = LabelFrame(LEFT_frame, bd=2, bg="white", relief=RIDGE, text="Department Information", font=("Times New Roman", 12, "bold"))
        Department_information.place(x=5, y=100, width=590, height=110)

        # department label
        dep_label = Label(Department_information, text="Commissionerate", font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(Department_information, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("select commissionerate", "rachakonda", "cyberabad", "warangal", "Nizamabad", "khammam")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        station_label = Label(Department_information, text="Station", font=("times new roman", 12, "bold"))
        station_label.grid(row=1, column=0, padx=10)

        station_combo = ttk.Combobox(Department_information, textvariable=self.var_station, font=("times new roman", 12, "bold"), state="readonly")
        station_combo["values"] = ("select station", "nagole", "uppal", "lbnagar", "Ibrahimpatnam")
        station_combo.current(0)
        station_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        criminal_details = LabelFrame(LEFT_frame, bd=2, bg="white", relief=RIDGE, text="criminal information", font=("times new roman", 12, "bold"))
        criminal_details.place(x=5, y=220, width=590, height=235)

        criminal_id = Label(criminal_details, text="Criminal ID", font=("times new roman", 12, "bold"))
        criminal_id.grid(row=0, column=0, padx=10)

        criminal_id_entry = ttk.Entry(criminal_details, textvariable=self.var_criminal_id, width=20, font=("times new roman", 13, "bold"))
        criminal_id_entry.grid(row=0, column=1, padx=10, sticky=W)

        Name = Label(criminal_details, text="Name", font=("times new roman", 12, "bold"))
        Name.grid(row=2, column=0, padx=10)

        Name_entry = ttk.Entry(criminal_details, textvariable=self.var_name, width=20, font=("times new roman", 13, "bold"))
        Name_entry.grid(row=2, column=1, padx=10, sticky=W)

        Gender = Label(criminal_details, text="Gender", font=("times new roman", 12, "bold"))
        Gender.grid(row=2, column=2, padx=10)

        Name_entry = ttk.Entry(criminal_details, textvariable=self.var_Gender, width=20, font=("times new roman", 13, "bold"))
        Name_entry.grid(row=2, column=3, padx=10, sticky=W)

        Age = Label(criminal_details, text="Age", font=("times new roman", 12, "bold"))
        Age.grid(row=6, column=0, padx=20)

        Age_entry = ttk.Entry(criminal_details, textvariable=self.var_Age, width=20, font=("times new roman", 13, "bold"))
        Age_entry.grid(row=6, column=1, padx=10, pady=10, sticky=W)

        DOB = Label(criminal_details, text="DOB", font=("times new roman", 12, "bold"))
        DOB.grid(row=6, column=2, padx=20)

        DOB_entry = ttk.Entry(criminal_details, textvariable=self.var_DOB, width=20, font=("times new roman", 13, "bold"))
        DOB_entry.grid(row=6, column=3, padx=10, pady=10, sticky=W)

        # radio Button
        RadioBtn1 = ttk.Radiobutton(criminal_details, text="take photo sample", variable=self.var_radio1, value="Yes")
        RadioBtn1.grid(row=12, column=2)

        # radio Button
        RadioBtn2 = ttk.Radiobutton(criminal_details, text="no photo sample", variable=self.var_radio1, value="No")
        RadioBtn2.grid(row=12, column=1)

        # buttons frame
        btn_frame = Frame(criminal_details, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=120, width=565, height=45)

        save_btn = Button(btn_frame, text="save", command=self.add_data, width=13, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=13, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="update", command=self.update_data, width=13, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="reset", width=13,command=self.reset_data,font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame = Frame(criminal_details, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=160, width=565, height=45)

        takephotosample_btn = Button(btn_frame, text="Take photo Sameple",command=self.generate_dataset,width=27, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        takephotosample_btn.grid(row=2, column=0)
        Updatephotosample_btn = Button(btn_frame, text="update photo Sameple", width=27, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        Updatephotosample_btn.grid(row=2, column=1)

        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="criminal details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=620, y=10, width=630, height=480)

        img_details = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\me.jpeg")
        img_details = img_details.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg_details = ImageTk.PhotoImage(img_details)
        f_lbl = Label(self.root, image=self.photoimg_details)
        f_lbl.place(x=700, y=180, width=500, height=100)

        # search system
        search_frame = LabelFrame(Right_frame, bg="white", relief=RIDGE, text="Search system", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=100, width=600, height=70)

        search_label = Label(search_frame, text="Search by:", bg="green", font=("times new roman", 12, "bold"))
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 8, "bold"), state="readonly")
        search_combo["values"] = ("select", "Name", "DOB", "Age")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.search_entry = ttk.Entry(search_frame, width=15, 
                                    font=("times new roman", 10, "bold"))
        self.search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search_btn = Button(search_frame, text="search", width=13, font=("times new roman", 10, "bold"), bg="blue", fg="white",command=self.search_data)
        search_btn.grid(row=0, column=3, padx=4)

        showall_btn = Button(search_frame, text="Show All", width=13, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        showall_btn.grid(row=0, column=4, padx=4)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=180, width=600, height=200)
        Scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        Scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.criminal_table = ttk.Treeview(table_frame, columns=("Criminal ID", "Commissionerate", "Station", "Name", "Gender", "DOB", "Age"), xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_x.config(command=self.criminal_table.xview)
        Scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading("Criminal ID", text="Criminal ID")
        self.criminal_table.heading("Commissionerate", text="Commissionerate")
        self.criminal_table.heading("Station", text="Station")
        self.criminal_table.heading("Name", text="Name")
        self.criminal_table.heading("Age", text="Age")
        self.criminal_table.heading("DOB", text="Date of Birth")
        self.criminal_table.heading("Gender", text="Gender")
        self.criminal_table["show"] = "headings"
        self.criminal_table.column("Criminal ID", width=100)
        self.criminal_table.column("Commissionerate", width=150)
        self.criminal_table.column("Station", width=150)
        self.criminal_table.column("Name", width=150)
        self.criminal_table.column("Age", width=150)
        self.criminal_table.column("DOB", width=150)
        self.criminal_table.column("Gender", width=150)

        self.criminal_table.pack(fill=BOTH, expand=0)
        self.criminal_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ======================== function declaration =======================
    def add_data(self):
        # Check if any of the required fields are empty
        if self.var_criminal_id.get() == "" or self.var_dep.get() == "select commissionerate" or self.var_name.get() == "" or self.var_Age.get() == "" or self.var_Gender.get() == "" or self.var_DOB.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="gnani@23wj1a6278", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO criminal(criminal_id, dep, station, name, age, gender, dob, photo_sample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_criminal_id.get(),
                    self.var_dep.get(),
                    self.var_station.get(),
                    self.var_name.get(),
                    self.var_Age.get(),
                    self.var_Gender.get(),
                    self.var_DOB.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Criminal details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="gnani@23wj1a6278", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM criminal")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    #======================get cursor==============================
    def get_cursor(self, event=""):
        cursor_focus = self.criminal_table.focus()
        content = self.criminal_table.item(cursor_focus)
        data = content["values"]

        self.var_criminal_id.set(data[0])
        self.var_dep.set(data[1])
        self.var_station.set(data[2])
        self.var_name.set(data[3])
        self.var_Gender.set(data[4])
        self.var_DOB.set(data[5])
        self.var_Age.set(data[6])
        self.var_radio1.set(data[7])
        

    #==========update function=====
    def get_db_connection(self):
        """Helper method to get a database connection"""
        return mysql.connector.connect(host="localhost", username="root", password="gnani@23wj1a6278", database="face_recognizer")

    def update_data(self):
        if self.var_criminal_id.get() == "" or self.var_dep.get() == "select commissionerate" or self.var_name.get() == "" or self.var_Age.get() == "" or self.var_Gender.get() == "" or self.var_DOB.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update the criminal details?", parent=self.root)
                if update:  # Check if 'Yes' was clicked
                    conn = self.get_db_connection()  # Reuse the DB connection method
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE criminal SET dep=%s, station=%s, name=%s, age=%s, gender=%s, dob=%s, photo_sample=%s WHERE criminal_id=%s", (
                        self.var_dep.get(),
                        self.var_station.get(),
                        self.var_name.get(),
                        self.var_Age.get(),
                        self.var_Gender.get(),
                        self.var_DOB.get(),
                        self.var_radio1.get(),  # Ensure this value is appropriate for photo_sample
                        self.var_criminal_id.get()
                    ))
                    conn.commit()  # Commit changes
                    self.fetch_data()  # Refresh the data
                    conn.close()
                    messagebox.showinfo("Success", "Criminal details updated successfully", parent=self.root)
            except mysql.connector.Error as err:  # Catching specific MySQL errors
                messagebox.showerror("Error", f"Database Error: {str(err)}", parent=self.root)
            except Exception as es:  # Catching other general exceptions
                messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_criminal_id.get() == "":
            messagebox.showerror("Error", "Please select a criminal from the list", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this criminal?", parent=self.root)
                if delete:  # Check if 'Yes' was clicked
                    conn = self.get_db_connection()  # Reuse the DB connection method
                    my_cursor = conn.cursor()
                    my_cursor.execute("DELETE FROM criminal WHERE criminal_id=%s", (self.var_criminal_id.get(),))
                    conn.commit()  # Commit after deletion
                    self.fetch_data()  # Refresh the data
                    conn.close()
                    messagebox.showinfo("Deleted", "Criminal details deleted successfully", parent=self.root)
                else:
                    return  # If 'No' was clicked, do nothing
            except mysql.connector.Error as err:  # Catching specific MySQL errors
                messagebox.showerror("Error", f"Database Error: {str(err)}", parent=self.root)
            except Exception as es:  # Catching other general exceptions
                messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)
  

    # reset
    def reset_data(self):
        self.var_criminal_id.set("")
        self.var_dep.set("select commissionerate")
        self.var_station.set("select station")
        self.var_name.set("")
        self.var_Age.set("")
        self.var_Gender.set("")
        self.var_DOB.set("")
        self.var_radio1.set("")

        #====================generate data set take photo samples ===================
    def generate_dataset(self):
        if self.var_criminal_id.get() == "" or self.var_dep.get() == "select commissionerate" or self.var_name.get() == "" or self.var_Age.get() == "" or self.var_Gender.get() == "" or self.var_DOB.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="gnani@23wj1a6278", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from criminal")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE criminal SET dep=%s, station=%s, name=%s, age=%s, gender=%s, dob=%s, photo_sample=%s WHERE criminal_id=%s", (
                        self.var_dep.get(),
                        self.var_station.get(),
                        self.var_name.get(),
                        self.var_Age.get(),
                        self.var_Gender.get(),
                        self.var_DOB.get(),
                        self.var_radio1.get(),
                        self.var_criminal_id.get()
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                

                #============== doad predifiend dataon face frontals from opencv================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum NEighbour=5


                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Crooped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)== 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed !!!")     
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    def search_data(self):
        search_by = self.search_combo.get()
        search_term = self.search_entry.get().strip()  # Added strip() to remove whitespace

        if search_by == "Select":
            messagebox.showerror("Error", "Please select a search criteria", parent=self.root)
            return
        
        if not search_term:
            messagebox.showerror("Error", "Please enter a search term", parent=self.root)
            return
        
        try:
            # Create a mapping of search criteria to column indices
            search_columns = {
                "Criminal ID": 0,
                "Name": 1,
                "Station": 2
            }
            
            # Get the column index safely
            col_index = search_columns.get(search_by, 0)
            
            # Filter the data with safety checks
            filtered_data = []
            for row in self.mydata:
                # Ensure the row has enough columns and the value exists
                if len(row) > col_index and search_term.lower() in str(row[col_index]).lower():
                    filtered_data.append(row)
            
            if not filtered_data:
                messagebox.showinfo("No Results", "No matching records found", parent=self.root)
                return
            
            self.current_data = filtered_data
            self.fetchData(filtered_data)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error during search: {str(e)}", parent=self.root)

            
# Run the application
if __name__ == "__main__":
    root = Tk()
    obj = criminal(root)
    root.mainloop()