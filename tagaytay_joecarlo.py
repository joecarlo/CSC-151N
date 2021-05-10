from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import os
import csv

class student:
    def __init__(self,root):
        self.root = root
        blank_space = " "
        self.root.title(200 * blank_space + "Student Information System")
        self.root.geometry("1150x475+0+0")
        self.root.config(bg="yellow")
        self.data = dict()
        self.temp = dict()
        self.filename = 'csc.csv'
        
        StudentIDNumber = StringVar()
        StudentName = StringVar()
        Course = StringVar()
        YearLevel = StringVar()
        Gender = StringVar()
        Search = StringVar()
        
        if not os.path.exists(self.filename):
            with open(self.filename,mode = 'w') as csv_file:
                fieldnames = ["ID Number","Name","Gender","Course","Year Level"]
                writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                writer.writeheader()
        
        else:
            with open(self.filename, newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    self.data[row["ID Number"]] = {'Name': row["Name"],'Gender': row["Gender"],' Course': row["Course"], 'Year Level': row["Year Level"]}
            self.temp = self.data.copy()
            
        def addData():
            with open(self.filename, "a", newline="") as file:
                csvfile = csv.writer(file)
                if StudentIDNumber.get() == "" or StudentName.get() == "" or YearLevel.get() == "":
                    tkinter.messagebox.showinfo("SIS", "Please Fill In the Box")
                else:
                    self.data[StudentIDNumber.get()] = {'Name': StudentName.get(), 'Gender': Gender.get(),
                                                   'Course': Course.get(),
                                                   'Year Level': YearLevel.get()}
                    self.saveData()
                    tkinter.messagebox.showinfo("SIS", "Student Recorded Successfully")
                #Clear()
                displayStudent()

        def displayStudent():
            tree.delete(*tree.get_children())
            with open(self.filename) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    studentid = row['ID Number']
                    Name = row['Name']
                    Gender = row['Gender']
                    Course = row['Course']
                    YearLevel = row['Year Level']
                    tree.insert("", 0, values=(studentid, Name, Gender, Course, YearLevel))

        def deleteData():
            x = tree.focus()
            if x == "":
                tkinter.messagebox.showerror("SIS", "Please select a record from the table.")
                return
            id_no = tree.item(x, "values")[0]
            
            self.data.pop(id_no, None)
            self.saveData()
            tree.delete(x)
            tkinter.messagebox.showinfo("SIS", "Student Record Deleted Successfully")
 
                
        def Clear():
            StudentIDNumber.set("")
            StudentName.set("") 
            YearLevel.set("")
            Gender.set("")
            Course.set("")
            
        def searchStudent():
            if self.Search.get() in self.data:
                vals = list(self.data[self.Search.get()].values())
                tree.delete(*tree.get_children())
                tree.insert("", 0, values=(self.Search.get(), vals[0], vals[1], vals[2], vals[3]))
            elif self.Search.get() == "":
                displayStudent()
            else:
                tkinter.messagebox.showerror("SIS", "Student not found.")
                return
            
        def editStudent():
            if tree.focus() == "":
                tkinter.messagebox.showerror("SIS", "Please select a record from the table.")
                return
            values = tree.item(tree.focus(), "values")
            StudentIDNumber.set(values[0])
            StudentName.set(values[1])
            Gender.set(values[2])
            Course.set(values[3])
            YearLevel.set(values[4]) 
        
        def updateStudent():
            with open(self.filename, "a", newline="") as file:
                csvfile = csv.writer(file)
                if StudentIDNumber.get() == "" or StudentName.get() == "" or YearLevel.get() == "":
                    tkinter.messagebox.showinfo("SIS", "Please Fill In the Box")
                else:
                    self.data[StudentIDNumber.get()] = {'Name': StudentName.get(), 'Gender': Gender.get(),
                                                   'Course': Course.get(),
                                                   'Year Level': YearLevel.get()}
                    self.saveData()
                    tkinter.messagebox.showinfo("SIS", "Student Recorded Successfully")
                Clear()
                displayStudent()   
        #==============================frame
        
        TitleFrame = Frame(self.root, bd=5, width=1000, bg="gray10",height=90, relief=RIDGE)
        TitleFrame.pack(side=TOP)
        
        LeftFrame1 = Frame(self.root,bg="yellow", bd=5, width=600, height=250, padx=2, pady=4)
        LeftFrame1.pack(side=LEFT,padx=0,pady=0)
        
        #============================title
        
        self.lblTitle = Label(TitleFrame, font=('arial', 40 , 'bold'), text="STUDENT INFORMATION SYSTEM",bg="gray10",fg="snow",bd=7)
        self.lblTitle.grid(row=0, column=0, padx=132)
        
         #========================labels and entry
        
        self.lblStudentID = Label(LeftFrame1, font=('arial', 13, 'bold'), bg="yellow",text="Student ID Number", bd=7, anchor=W)
        self.lblStudentID.grid(row=0, column=0)
        self.lblStudentID = Label(LeftFrame1, font=('arial', 10), bg="yellow", text="yyyy-nnnn", bd=7, anchor=W)
        self.lblStudentID.grid(row=1, column=1)
        self.lblStudentID = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=7, width=48, justify='left', textvariable = StudentIDNumber)
        self.lblStudentID.grid(row=0, column=1)
        
        self.lblFullName = Label(LeftFrame1, font=('arial', 13, 'bold'),bg="yellow", text="Full Name", bd=7, anchor=W)
        self.lblFullName.grid(row=2, column=0)
        self.lblFullName = Label(LeftFrame1, font=('arial', 10),bg="yellow", text="Lastname, Firstname Middleinitial", bd=7, anchor=W)
        self.lblFullName.grid(row=3, column=1)
        self.lblFullName = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=7, width=48, textvariable = StudentName)
        self.lblFullName.grid(row=2, column=1)
        
        self.lblCourse = Label(LeftFrame1, font=('arial', 13, 'bold'),bg="yellow", text="Course", bd=7, anchor=W)
        self.lblCourse.grid(row=4, column=0)
        self.lblCourse = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=7, width=48, justify='left', textvariable = Course)
        self.lblCourse.grid(row=4, column=1)
        
        self.lblYearLevel = Label(LeftFrame1, font=('arial', 13, 'bold'), bg="yellow",text="Year Level", bd=7, anchor=W)
        self.lblYearLevel.grid(row=5, column=0)
        self.lblYearLevel= ttk.Combobox(LeftFrame1, font=('arial', 10, 'bold'), state='readonly', width=47, textvariable = YearLevel)
        self.lblYearLevel['values'] = ('','1st Year','2nd Year','3rd Year','4th Year','5th Year')
        self.lblYearLevel.current(0)
        self.lblYearLevel.grid(row=5, column=1)
        
        self.lblGender = Label(LeftFrame1, font=('arial', 13, 'bold'),bg="yellow", text="Gender", bd=7, anchor=W)
        self.lblGender.grid(row=6, column=0)
        self.lblGender = ttk.Combobox(LeftFrame1, font=('arial', 10, 'bold'), state='readonly', width=47, textvariable = Gender)
        self.lblGender['values'] = ('','Female','Male')
        self.lblGender.current(0)
        self.lblGender.grid(row=6, column=1)
        
        self.Search = Entry(self.root, font=("Poppins", 10), textvariable=Search, width=19)
        self.Search.place(x=560,y=100)
        self.Search.insert(0,'Search ID Number')
        #=====================buttons
        
        self.btnAddNew=Button(self.root, pady=1,bd=4,font=('arial',10,'bold'), padx=24, width=8, text='ADD', command = addData)
        self.btnAddNew.place(x=15,y=410)

        self.btnUpdate=Button(self.root, pady=1,bd=4,font=('arial',10,'bold'), padx=24, width=8, text='UPDATE', command = updateStudent)
        self.btnUpdate.place(x=150,y=410)

        self.btnDelete=Button(self.root, pady=1,bd=4,font=('arial',10,'bold'), padx=24, width=8, text='DELETE',command = deleteData)
        self.btnDelete.place(x=285,y=410)

        self.btnClear=Button(self.root, pady=1,bd=4,font=('arial',10,'bold'), padx=24, width=8, text='CLEAR', command=Clear)
        self.btnClear.place(x=420,y=410)
        
        self.btnSearch=Button(self.root, pady=1,bd=4,font=('arial',10,'bold'), padx=24, width=8, text='SEARCH', command = searchStudent)
        self.btnSearch.place(x=710,y=95)
        
        self.btnRefresh=Button(self.root, pady=1,bd=4,font=('arial',10,'bold'), padx=24, width=8, text='SHOW ALL', command=displayStudent)
        self.btnRefresh.place(x=855,y=95)
        
        self.btnSelect=Button(self.root, pady=1,bd=4,font=('arial',10,'bold'), padx=24, width=8, text='SELECT',command = editStudent)
        self.btnSelect.place(x=1000,y=95)
                
        #======================treeview
        
        scroll_y=Scrollbar(self.root, orient=VERTICAL)
        tree = ttk.Treeview(self.root,height = 15,columns=("ID Number", "Name", "Gender", "Course", "Year Level"),
                                        yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.place(x=1130,y=128,height=330)
    
        tree.heading("ID Number", text="ID Number")
        tree.heading("Name", text="Name")
        tree.heading("Course", text="Course")
        tree.heading("Year Level", text="Year Level")
        tree.heading("Gender", text="Gender")
        tree['show'] = 'headings'
        tree.column("ID Number", width=90)
        tree.column("Name", width=180)
        tree.column("Course", width=99)
        tree.column("Year Level", width=99)
        tree.column("Gender", width=93)
        scroll_y.config(command=tree.yview)
        tree.pack(fill=BOTH,expand=1)
        tree.place(x=560,y=130)
        
        displayStudent()
                
    def saveData(self):
        datalist = []
        with open(self.filename, "w", newline='') as u:
            fieldnames = ["ID Number", "Name", "Gender", "Course", "Year Level"]
            writer = csv.DictWriter(u, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for id, val in self.data.items():
                temp = {"ID Number": id}
                for key, value in val.items():
                    temp[key] = value
                datalist.append(temp)
            writer.writerows(datalist)
            
if __name__=='__main__':
    root = Tk()
    application = student(root) 
    root.mainloop()       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
