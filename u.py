from tkinter import ttk
import tkinter as tk
from datetime import date
from tkinter import *
import sqlite3

class Database:
    def __init__(self, filename):
        self.filename = filename
        self.con = sqlite3.connect(self.filename)
        self.cur = self.con.cursor()
        self.create_table()
        self.rows = self.fetch()

    def create_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS st(
            name_val text,
            age_val text,
            gender_val text,
            email_val text,
            guardian_val text,
            number_val text,
            live_val text,
            date_val text
        )
        """

        self.cur.execute(sql)
        self.con.commit()

    def insert(self, name_val, age_val,gender_val,email_val,guardian_val,number_val,live_val,date_val):
        self.cur.execute("insert into st values (?,?,?,?,?,?,?,?)",
                         (name_val, age_val, gender_val,email_val, guardian_val,number_val,live_val,date_val))
        self.con.commit()
        self.rows = self.fetch()

    def fetch(self):
        self.cur.execute("SELECT * FROM st")
        rows = self.cur.fetchall()
        return rows

    def remove(self,name_val):
        self.cur.execute("DELETE FROM st WHERE name_val = ?", (name_val,))
        self.con.commit()
        self.rows = self.fetch()

    def update(self, name_val, age_val,gender_val,email_val,guardian_val,number_val,live_val,date_val):
        self.cur.execute("Update st set name_val=?,age_val=?,gender_val=?,email_val=?,guardian_val=?,number_val=?,live_val=?,date_val=?",
                         (name_val, age_val, gender_val, email_val, guardian_val, number_val, live_val, date_val))
        self.con.commit()
        self.rows = self.fetch()


data_sql = Database("Employee.sql")

...






#################################################

today = date.today()


s = Tk()



width = s.winfo_screenwidth()
height = s.winfo_screenheight()

s.geometry("%dx%d" % (width, height))

l20=Label(s, text="Search :",width=10, font=("NORMAL", "30"))
l20.place(x=-30, y=340)

ser = Entry(s, font=("NORMAL", "20"), width=87)
ser.place(x=200, y=350)


l1=Label(s, text="Full-Name :", font=("NORMAL", "20"))
l1.place(x=5, y=5)
l3=Label(s, text="Live in :", font=("NORMAL", "20"))
l3.place(x=5, y=50)
l4=Label(s, text="E-mail :", font=("NORMAL", "20"))
l4.place(x=5, y=95)
l10=Label(s, text="Date :", font=("NORMAL", "20"))
l10.place(x=5, y=140)

l5=Label(s, text="Number :", font=("NORMAL", "20"))
l5.place(x=790, y=4)
l8=Label(s, text="Guardian :", font=("NORMAL", "20"))
l8.place(x=790, y=50)
l9=Label(s, text="Gender :", font=("NORMAL", "20"))
l9.place(x=790, y=95)
l11=Label(s, text="Age :", font=("NORMAL", "20"))
l11.place(x=790, y=145)


name = Entry(s, font=("NORMAL", "20"), width=29)
name.place(x=190, y=5)


live = Entry(s, font=("NORMAL", "20"), width=29)
live.place(x=190, y=50)

email = Entry(s, font=("NORMAL", "20"), width=29)
email.place(x=190, y=95)

number = Entry(s, font=("NORMAL", "20"), width=38)
number.place(x=940, y=5)

guardian = Entry(s, font=("NORMAL", "20"), width=38)
guardian.place(x=940, y=50)

age = Entry(s, font=("NORMAL", "20"), width=38)
age.place(x=940, y=150)

comboGender1 = ttk.Combobox(s,font=(NORMAL,28), state="readonly", width=26)
comboGender1["values"] = ("Male","Female","- - - - - - - -")
comboGender1.place(x=940, y=95)

comboGender2 = ttk.Combobox(s,font=(NORMAL,28), state="readonly", width=20)
comboGender2["values"] = (today)
comboGender2.place(x=190, y=140)




def SAVE():
    # get the data from the entry widgets
    name_val = name.get()
    email_val = email.get()
    number_val = number.get()
    live_val = live.get()
    guardian_val = guardian.get()
    gender_val = comboGender1.get()
    date_val = comboGender2.get()
    age_val = age.get()

    data_sql.insert(
        name_val,
        email_val,
        number_val,
        live_val,
        guardian_val,
        gender_val,
        date_val,
        age_val)

    tree.insert('', tk.END, values=(name_val, email_val, number_val, live_val, guardian_val, gender_val, date_val, age_val))



def delete_tree():
    selected_item = tree.selection()[0]
    name_val = tree.set(selected_item, '#1')
    tree.delete(selected_item)
    data_sql.remove(name_val)

    name.delete(0, tk.END)
    email.delete(0, tk.END)
    number.delete(0, tk.END)
    live.delete(0, tk.END)
    guardian.delete(0, tk.END)
    age.delete(0, tk.END)
    comboGender1.set("")
    comboGender2.set("")




def Save_the_update():
    SAVE()
    delete_tree()


save = Button(s,text="Save",width=44,font=(NORMAL,20),bg="#32ae85",command=SAVE)
save.place(x=800,y=210)

update = Button(s,text="Save the update",width=38,font=(NORMAL,20),bg="#32ae85",command=Save_the_update)
update.place(x=12,y=270)

delete = Button(s,text="Delete",width=38,font=(NORMAL,20),bg="#32ae85",command=delete_tree)
delete.place(x=12,y=210)



tree = ttk.Treeview(s,columns=("Name", "E-mail", "Number", "Live in", "Guardian", "Gender", "Date", "Age"), selectmode="extended", height=20)

tree.heading("Name", text="Name")
tree.heading("E-mail", text="E-mail")
tree.heading("Number", text="Number")
tree.heading("Live in", text="Live in")
tree.heading("Guardian", text="Guardian")
tree.heading("Gender", text="Gender")
tree.heading("Date", text="Date")
tree.heading("Age", text="Age")


def treeview_click(event):

    item = tree.item(tree.selection())
    name_val, email_val, number_val, live_val, guardian_val, gender_val, date_val, age_val = item["values"]

    name.delete(0, tk.END)
    name.insert(0, name_val)
    email.delete(0, tk.END)
    email.insert(0, email_val)
    number.delete(0, tk.END)
    number.insert(0, number_val)
    live.delete(0, tk.END)
    live.insert(0, live_val)
    guardian.delete(0, tk.END)
    guardian.insert(0, guardian_val)
    comboGender1.set(gender_val)
    comboGender2.set(date_val)
    age.delete(0, tk.END)
    age.insert(0, age_val)


gt = tree.bind("<<TreeviewSelect>>", treeview_click)





for row in data_sql.rows:
    tree.insert('', tk.END, values=row)

tree.place(x=-200, y=400)


def light():
    s.config(bg="#EEEEEE")

    l1.config(bg="#EEEEEE",fg="#181818")
    l3.config(bg="#EEEEEE", fg="#181818")
    l4.config(bg="#EEEEEE", fg="#181818")
    l5.config(bg="#EEEEEE", fg="#181818")
    l8.config(bg="#EEEEEE", fg="#181818")
    l9.config(bg="#EEEEEE", fg="#181818")
    l10.config(bg="#EEEEEE", fg="#181818")
    l20.config(bg="#EEEEEE", fg="#181818")
    l11.config(bg="#EEEEEE", fg="#181818")

    dark = Button(s, text="Dark-mode", width=44, font=(NORMAL, 20),bg="#32ae85", command=darke)
    dark.place(x=800, y=270)

def darke():
    s.config(bg="#181818")

    l1.config(bg="#181818",fg="#EEEEEE")
    l3.config(bg="#181818", fg="#EEEEEE")
    l4.config(bg="#181818", fg="#EEEEEE")
    l5.config(bg="#181818", fg="#EEEEEE")
    l8.config(bg="#181818", fg="#EEEEEE")
    l9.config(bg="#181818", fg="#EEEEEE")
    l10.config(bg="#181818", fg="#EEEEEE")
    l20.config(bg="#181818", fg="#EEEEEE")
    l11.config(bg="#181818", fg="#EEEEEE")


    whi = Button(s, text="Light-mode", width=44, font=(NORMAL, 20),bg="#32ae85", command=light)
    whi.place(x=800, y=270)


dark = Button(s,text="Dark-mode",width=44,font=(NORMAL,20),bg="#32ae85",command=darke)
dark.place(x=800,y=270)
dark.invoke()


s.mainloop()
