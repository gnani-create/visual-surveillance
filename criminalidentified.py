from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import csv 
from tkinter import filedialog

class CriminalIdentified:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System to Identify the Criminals")
        self.mydata = []  # Initialize mydata as instance variable
        self.current_data = []  # To store currently displayed data
        
        #================variables==================
        self.var_criminal_id = StringVar()
        self.var_criminal_Name = StringVar()
        self.var_criminal_Station = StringVar()
        self.var_criminal_Time = StringVar()
        self.var_criminal_date = StringVar()
        self.var_criminal_crime = StringVar()
        self.var_criminal_Age = StringVar()
        self.var_criminal_Lastlocation = StringVar()

        # Top Images
        try:
            img = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\magnifier-fingerprint-police-form-background-260nw-2337603653.webp")
            img = img.resize((500, 130), Image.Resampling.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)
            f_lbl = Label(self.root, image=self.photoimg)
            f_lbl.place(x=0, y=0, width=500, height=100)
        except:
            f_lbl = Label(self.root, text="Image 1 not found", bg="white")
            f_lbl.place(x=0, y=0, width=500, height=100)

        try:
            img = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\my img.jpg")
            img = img.resize((500, 130), Image.Resampling.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img)
            f_lbl2 = Label(self.root, image=self.photoimg1)
            f_lbl2.place(x=500, y=0, width=400, height=100)
        except:
            f_lbl2 = Label(self.root, text="Image 2 not found", bg="white")
            f_lbl2.place(x=500, y=0, width=400, height=100)

        try:
            img = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\images.jpeg")
            img = img.resize((500, 130), Image.Resampling.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img)
            f_lbl3 = Label(self.root, image=self.photoimg2)
            f_lbl3.place(x=900, y=0, width=500, height=100)
        except:
            f_lbl3 = Label(self.root, text="Image 3 not found", bg="white")
            f_lbl3.place(x=900, y=0, width=500, height=100)

        # Title
        title_lbl = Label(self.root, text="Criminal Identification", 
                         font=("Times New Roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=100, width=1530, height=40)

        # Main Frame
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=0, y=140, width=1530, height=650)

        # Left Frame
        LEFT_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                              text="Identified details", font=("times new roman", 12, "bold"))
        LEFT_frame.place(x=15, y=10, width=600, height=630)

        try:
            img_left = Image.open(r"c:\Users\GNANESHWAR\Desktop\face\crime.jpeg")
            img_left = img_left.resize((500, 130), Image.Resampling.LANCZOS)
            self.photoimg_left = ImageTk.PhotoImage(img_left)
            f_lbl = Label(LEFT_frame, image=self.photoimg_left)
            f_lbl.place(x=15, y=0, width=500, height=100)
        except:
            f_lbl = Label(LEFT_frame, text="Crime Image not found", bg="white")
            f_lbl.place(x=15, y=0, width=500, height=100)

        left_inside_frame = Frame(LEFT_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=120, width=585, height=400)

        # Criminal ID
        criminal_id = Label(left_inside_frame, text="Criminal ID:", 
                          font=("times new roman", 12, "bold"))
        criminal_id.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.criminal_id_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_criminal_id,
                                         font=("times new roman", 13, "bold"))
        self.criminal_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Name
        Name = Label(left_inside_frame, text="Name:", 
                    font=("times new roman", 12, "bold"))
        Name.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        self.Name_entry = ttk.Entry(left_inside_frame, width=13, textvariable=self.var_criminal_Name,
                                  font=("times new roman", 13, "bold"))
        self.Name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Gender
        Gender = Label(left_inside_frame, text="Gender:", 
                      font=("times new roman", 12, "bold"))
        Gender.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        self.gender_combo = ttk.Combobox(left_inside_frame, 
                                       font=("times new roman", 12), 
                                       width=18, state="readonly")
        self.gender_combo["values"] = ("Male", "Female", "Other")
        self.gender_combo.current(0)
        self.gender_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Age
        Age = Label(left_inside_frame, text="Age:", 
                   font=("times new roman", 12, "bold"))
        Age.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        self.Age_entry = ttk.Entry(left_inside_frame, width=13, textvariable=self.var_criminal_Age,
                                 font=("times new roman", 13, "bold"))
        self.Age_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # lastlocation
        lastlocation = Label(left_inside_frame, text="Lastlocation:", 
                   font=("times new roman", 12, "bold"))
        lastlocation.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        self.lastlocation_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_criminal_Lastlocation,
                                 font=("times new roman", 13, "bold"))
        self.lastlocation_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Time
        Time = Label(left_inside_frame, text="Time:", 
                       font=("times new roman", 12, "bold"))
        Time.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        self.Time_entry = ttk.Entry(left_inside_frame, width=13, textvariable=self.var_criminal_Time,
                                     font=("times new roman", 13, "bold"))
        self.Time_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Station
        Station = Label(left_inside_frame, text="Police Station:", 
                       font=("times new roman", 12, "bold"))
        Station.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.Station_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_criminal_Station,
                                     font=("times new roman", 13, "bold"))
        self.Station_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

      

        # Buttons Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=580, height=35)

        save_btn = Button(btn_frame, text="Import CSV", command=self.importcsv,
                         width=17, font=("times new roman", 10, "bold"), 
                         bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export CSV", command=self.exportcsv, width=17, 
                           font=("times new roman", 10, "bold"), 
                           bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", width=17, 
                           font=("times new roman", 10, "bold"), 
                           bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=17, 
                          font=("times new roman", 10, "bold"), 
                          bg="blue", fg="white", command=self.reset_fields)
        reset_btn.grid(row=0, column=3)

        # Right Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                               text="Other details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=620, y=10, width=880, height=630)

        # Search System
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
                                text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=5, width=870, height=70)

        search_label = Label(Search_frame, text="Search By:", 
                           font=("times new roman", 12, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.search_combo = ttk.Combobox(Search_frame, 
                                       font=("times new roman", 12), 
                                       width=15, state="readonly")
        self.search_combo["values"] = ("Select", "Criminal ID", "Name", "Station")
        self.search_combo.current(0)
        self.search_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        self.search_entry = ttk.Entry(Search_frame, width=15, 
                                    font=("times new roman", 13, "bold"))
        self.search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search_btn = Button(Search_frame, text="Search", width=12, 
                           font=("times new roman", 12, "bold"), 
                           bg="blue", fg="white", command=self.search_data)
        search_btn.grid(row=0, column=3, padx=5)

        showAll_btn = Button(Search_frame, text="Show All", width=12, 
                            font=("times new roman", 12, "bold"), 
                            bg="blue", fg="white", command=self.show_all_data)
        showAll_btn.grid(row=0, column=4, padx=5)

        # Table Frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=80, width=600, height=400)

        # Scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Treeview
        self.criminal_table = ttk.Treeview(table_frame, 
                                   columns=("id", "name", "station", "Age", 
                                           "Time", "Date", "Lastlocation", "crime"),
                                   xscrollcommand=scroll_x.set, 
                                   yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading("id", text="Criminal ID")
        self.criminal_table.heading("name", text="Name")
        self.criminal_table.heading("station", text="Station")
        self.criminal_table.heading("Age", text="Age")
        self.criminal_table.heading("Date", text="Date")
        self.criminal_table.heading("Time", text="Time")
        self.criminal_table.heading("Lastlocation", text="Lastlocation")
        

        self.criminal_table["show"] = "headings" 

        self.criminal_table.column("id", width=100)
        self.criminal_table.column("name", width=100)
        self.criminal_table.column("station", width=100)
        self.criminal_table.column("Age", width=100)
        self.criminal_table.column("Date", width=100)
        self.criminal_table.column("Time", width=100)
        self.criminal_table.column("Lastlocation", width=100)
        

        self.criminal_table.pack(fill=BOTH, expand=1)
        self.criminal_table.bind("<ButtonRelease-1>", self.get_cursor)

    def fetchData(self, rows):
        self.criminal_table.delete(*self.criminal_table.get_children())
        for i in rows:
            self.criminal_table.insert("", END, values=i)

    def importcsv(self):
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
            parent=self.root
        )
        if fln:
            try:
                with open(fln) as myfile:
                    csvread = csv.reader(myfile, delimiter=",")
                    self.mydata = []
                    for i in csvread:
                        # Ensure each row has at least 8 columns (pad with empty strings if needed)
                        while len(i) < 8:
                            i.append("")
                        self.mydata.append(i)
                    self.current_data = self.mydata.copy()
                    self.fetchData(self.mydata)
                    messagebox.showinfo("Success", f"Loaded {len(self.mydata)} records", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read file: {str(e)}", parent=self.root)

    def exportcsv(self):
        try:
            if len(self.mydata) < 1:
                messagebox.showerror("No data", "No data found to export", parent=self.root)
                return False
            
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                defaultextension=".csv",
                parent=self.root
            )
            
            if fln:
                with open(fln, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    for i in self.mydata:
                        exp_write.writerow(i)
                messagebox.showinfo("Data Export", f"Your data exported to {os.path.basename(fln)} successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export file: {str(e)}")

    def search_data(self):
        search_by = self.search_combo.get()
        search_term = self.search_entry.get().strip()

        if search_by == "Select":
            messagebox.showerror("Error", "Please select a search criteria", parent=self.root)
            return
        
        if not search_term:
            messagebox.showerror("Error", "Please enter a search term", parent=self.root)
            return
        
        try:
            search_columns = {
                "Criminal ID": 0,
                "Name": 1,
                "Station": 2
            }
            
            col_index = search_columns.get(search_by, 0)
            
            filtered_data = []
            for row in self.mydata:
                if len(row) > col_index and search_term.lower() in str(row[col_index]).lower():
                    filtered_data.append(row)
            
            if not filtered_data:
                messagebox.showinfo("No Results", "No matching records found", parent=self.root)
                return
            
            self.current_data = filtered_data
            self.fetchData(filtered_data)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error during search: {str(e)}", parent=self.root)

    def show_all_data(self):
        if not self.mydata:
            messagebox.showinfo("No Data", "No data available to display", parent=self.root)
            return
        
        self.current_data = self.mydata.copy()
        self.fetchData(self.mydata)

    def get_cursor(self, event):
        cursor_row = self.criminal_table.focus()
        content = self.criminal_table.item(cursor_row)
        rows = content['values']
        
        if rows:  # Check if there are values
            try:
                self.var_criminal_id.set(rows[0] if len(rows) > 0 else "")
                self.var_criminal_Name.set(rows[1] if len(rows) > 1 else "")
                self.var_criminal_Station.set(rows[2] if len(rows) > 2 else "")
                self.var_criminal_Age.set(rows[3] if len(rows) > 3 else "")
                self.var_criminal_Time.set(rows[4] if len(rows) > 4 else "")
                self.var_criminal_date.set(rows[5] if len(rows) > 5 else "")
                self.var_criminal_Lastlocation.set(rows[6] if len(rows) > 6 else "")
                # Assuming location is at index 6 (not mapped to a variable)
                self.var_criminal_crime.set(rows[7] if len(rows) > 7 else "")
            except IndexError:
                pass  # Handle cases where row doesn't have all columns

    def reset_fields(self):
        self.var_criminal_id.set("")
        self.var_criminal_Name.set("")
        self.var_criminal_Station.set("")
        self.var_criminal_Age.set("")
        self.var_criminal_Time.set("")
        self.var_criminal_date.set("")
        self.var_criminal_Lastlocation.set("")
        self.search_entry.delete(0, END)
        self.search_combo.current(0)
        self.show_all_data()

if __name__ == "__main__":
    root = Tk()
    obj = CriminalIdentified(root)
    root.mainloop()