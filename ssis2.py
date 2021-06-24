import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3

class SSIS:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Information System")
        self.root.geometry("1520x790+0+0")
        self.root.resizable(False, False)
                
        Course_Code = StringVar()
        Course_Name = StringVar()
        SearchBar_Var = StringVar()
        
        def connectCourse():
            conn = sqlite3.connect("StudentDatabase.db")
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("CREATE TABLE IF NOT EXISTS courses (Course_Code TEXT PRIMARY KEY, Course_Name TEXT)") 
            conn.commit() 
            conn.close()
            
        def addCourse():
            conn = sqlite3.connect("StudentDatabase.db")
            c = conn.cursor()         
            c.execute("INSERT INTO courses(Course_Code,Course_Name) VALUES (?,?)",\
                      (Course_Code.get(),Course_Name.get()))        
            conn.commit()       
            clearCourse()
            conn.close() 
            tkinter.messagebox.showinfo("Student Information System", "Course Recorded Successfully")
            displayCourse()
              
        def displayCourse():
            self.courselist.delete(*self.courselist.get_children())
            conn = sqlite3.connect("StudentDatabase.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM courses")
            rows = cur.fetchall()
            for row in rows:
                self.courselist.insert("", tk.END, text=row[0], values=row[0:])
            conn.close()
        
        def updateCourse():
            for selected in self.courselist.selection():
                conn = sqlite3.connect("StudentDatabase.db")
                cur = conn.cursor()
                cur.execute("PRAGMA foreign_keys = ON")
                cur.execute("UPDATE courses SET Course_Code=?, Course_Name=? WHERE Course_Code=?", \
                            (Course_Code.get(),Course_Name.get(), self.courselist.set(selected, '#1')))                       
                conn.commit()
                tkinter.messagebox.showinfo("Student Information System", "Course Updated Successfully")
                displayCourse()
                clearCourse()
                conn.close()
                
        def editCourse():
            x = self.courselist.focus()
            if x == "":
                tkinter.messagebox.showerror("Student Information System", "Please select a record from the table.")
                return
            values = self.courselist.item(x, "values")
            Course_Code.set(values[0])
            Course_Name.set(values[1])
                    
        def deleteCourse(): 
            try:
                messageDelete = tkinter.messagebox.askyesno("SSIS", "Do you want to permanently delete this record?")
                if messageDelete > 0:   
                    con = sqlite3.connect("StudentDatabase.db")
                    cur = con.cursor()
                    x = self.courselist.selection()[0]
                    id_no = self.courselist.item(x)["values"][0]
                    cur.execute("PRAGMA foreign_keys = ON")
                    cur.execute("DELETE FROM courses WHERE Course_Code = ?",(id_no,))                   
                    con.commit()
                    self.courselist.delete(x)
                    tkinter.messagebox.askyesno("Student Information System", "Course Deleted Successfully")
                    displayCourse()
                    con.close()                    
            except:
                tkinter.messagebox.showerror("Student Information System", "Students are still enrolled in this course")
                
        def searchCourse():
            Course_Code = SearchBar_Var.get()                
            con = sqlite3.connect("StudentDatabase.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM courses WHERE Course_Code = ?",(Course_Code,))
            con.commit()
            self.courselist.delete(*self.courselist.get_children())
            rows = cur.fetchall()
            for row in rows:
                self.courselist.insert("", tk.END, text=row[0], values=row[0:])
            con.close()
 
        def RefreshCourse():
            displayCourse()
        
        def clearCourse():
            Course_Code.set('')
            Course_Name.set('') 

        

        def connect():
            conn = sqlite3.connect("StudentDatabase.db")
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("CREATE TABLE IF NOT EXISTS studentdatabase (Student_ID TEXT PRIMARY KEY, Student_Name TEXT, Student_Course TEXT, \
                      Student_YearLevel TEXT, Student_Gender TEXT, \
                      FOREIGN KEY(Student_Course) REFERENCES courses(Course_Code) ON UPDATE CASCADE)") 
            conn.commit() 
            conn.close()    
        
        def addData():
            if Student_ID.get() == "" or Student_Name.get() == "" or Student_Course.get() == "" or Student_YearLevel.get() == "" or Student_Gender.get() == "": 
                tkinter.messagebox.showinfo("Student Information System", "Please fill in the box with *")
            else:  
                ID = Student_ID.get()
                ID_list = []
                for i in ID:
                    ID_list.append(i)
                a = ID.split("-")
                if len(a[0]) == 4:        
                    if "-" in ID_list:
                        if len(a[1]) == 1:
                            tkinter.messagebox.showerror("Student Information System", "Invalid ID\nID Number Format:YYYY-NNNN")
                        elif len(a[1]) ==2:
                            tkinter.messagebox.showerror("Student Information System", "Invalid ID\nIID Number Format:YYYY-NNNN")
                        elif len(a[1]) ==3:
                            tkinter.messagebox.showerror("Student Information System", "Invalid ID\nIID Number Format:YYYY-NNNN")
                        else:
                            x = ID.split("-")  
                            year = x[0]
                            number = x[1]
                            if year.isdigit()==False or number.isdigit()==False:
                                try:
                                    tkinter.messagebox.showerror("Student Information System", "Invalid ID")
                                except:
                                    pass
                            elif year==" " or number==" ":
                                try:
                                    tkinter.messagebox.showerror("Student Information System", "Invalid ID")
                                except:
                                    pass
                            else:
                                try:
                                    conn = sqlite3.connect("StudentDatabase.db")
                                    c = conn.cursor() 
                                    c.execute("PRAGMA foreign_keys = ON")                                                                                                              
                                    c.execute("INSERT INTO studentdatabase(Student_ID,Student_Name,Student_Course,Student_YearLevel,Student_Gender) VALUES (?,?,?,?,?)",\
                                                          (Student_ID.get(),Student_Name.get(),Student_Course.get(),Student_YearLevel.get(), Student_Gender.get()))                                       
                                                                       
                                    tkinter.messagebox.showinfo("Student Information System", "Student Recorded Successfully")
                                    conn.commit() 
                                    clear()
                                    displayData()
                                    conn.close()
                                except:
                                    tkinter.messagebox.showerror("Student Information System", "Course Unavailable")
                    else:
                        tkinter.messagebox.showerror("Student Information System", "Invalid ID")
                else:
                    tkinter.messagebox.showerror("Student Information System", "Invalid ID")
                 
        def updateData():
            if Student_ID.get() == "" or Student_Name.get() == "" or Student_Course.get() == "" or Student_YearLevel.get() == "" or Student_Gender.get() == "": 
                tkinter.messagebox.showinfo("Student Information System", "Please select a student")
            else:
                try:
                    for selected in self.studentlist.selection():
                        conn = sqlite3.connect("StudentDatabase.db")
                        cur = conn.cursor()
                        cur.execute("PRAGMA foreign_keys = ON")
                        cur.execute("UPDATE studentdatabase SET Student_ID=?, Student_Name=?, Student_Course=?, Student_YearLevel=?,Student_Gender=?\
                              WHERE Student_ID=?", (Student_ID.get(),Student_Name.get(),Student_Course.get(),Student_YearLevel.get(), Student_Gender.get(),\
                                  self.studentlist.set(selected, '#1')))
                        conn.commit()
                        tkinter.messagebox.showinfo("Student Information System", "Student Updated Successfully")
                        displayData()
                        clear()
                        conn.close()
                except:
                    tkinter.messagebox.showerror("Student Information System", "Cannot Update Student")
        
        def deleteData():   
            try:
                messageDelete = tkinter.messagebox.askyesno("Student Information System", "Do you want to permanently delete this record?")
                if messageDelete > 0:   
                    con = sqlite3.connect("StudentDatabase.db")
                    cur = con.cursor()
                    x = self.studentlist.selection()[0]
                    id_no = self.studentlist.item(x)["values"][0]
                    cur.execute("DELETE FROM studentdatabase WHERE Student_ID = ?",(id_no,))                   
                    con.commit()
                    self.studentlist.delete(x)
                    tkinter.messagebox.showinfo("Student Information System", "Student Deleted Successfully")
                    displayData()
                    con.close()                    
            except Exception as e:
                print(e)
                
        def searchData():
            Student_ID = SearchBar_Var.get()
            try:  
                con = sqlite3.connect("StudentDatabase.db")
                cur = con.cursor()
                cur .execute("PRAGMA foreign_keys = ON")
                cur.execute("SELECT * FROM studentdatabase")
                con.commit()
                self.studentlist.delete(*self.studentlist.get_children())
                rows = cur.fetchall()
                for row in rows:
                    if row[0].startswith(Student_ID):
                        self.studentlist.insert("", tk.END, text=row[0], values=row[0:])
                con.close()
            except:
                tkinter.messagebox.showerror("Student Information System", "Invalid ID")           
                
        def displayData():
            self.studentlist.delete(*self.studentlist.get_children())
            conn = sqlite3.connect("StudentDatabase.db")
            cur = conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("SELECT * FROM studentdatabase")
            rows = cur.fetchall()
            for row in rows:
                self.studentlist.insert("", tk.END, text=row[0], values=row[0:])
            conn.close()
                            
        def editData():
            x = self.studentlist.focus()
            if x == "":
                tkinter.messagebox.showerror("Student Information System", "Please select a record from the table.")
                return
            values = self.studentlist.item(x, "values")
            Student_ID.set(values[0])
            Student_Name.set(values[1])
            Student_Course.set(values[2])
            Student_YearLevel.set(values[3])
            Student_Gender.set(values[4])
            
        def Refresh():
            displayData()
        
        def clear():
            Student_ID.set('')
            Student_Name.set('') 
            Student_YearLevel.set('')
            Student_Gender.set('')
            Student_Course.set('')
            



if __name__ == '__main__':
    root = Tk()
    application = SSIS(root)
    root.mainloop()