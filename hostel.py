from tkinter import *
from tkinter import messagebox
import datetime
import sqlite3


def remove():
    inputBox.delete(0, END)
    inputBox1.delete(0, END)


def Login():
    base = Tk()
    base.geometry("800x700")
    base.title("Girls Hostel managment ")
    fnt = ("Arial", 14)
    def Del_Info():
        def delete():
            a = str(tex1.get())
            con = sqlite3.connect("hostel.db")
            q = "delete from  girls where sh_roll=" + a
            con.execute(q)
            con.commit()
            con.close()
            print("Succefully inserted....!!")
            messagebox.showinfo("DELETE", "Data  Deleted  sucessfully...")
            print("data DELETED")

        def Back():
            base5.destroy()
            Login()
            base.mainloop()

        base5 = Tk()
        base5.geometry("800x700")
        base5.title("Add New Girl ")
        fnt = ("Arial", 16)
        lab1 = Label(base5, text="Enter Hostel Roll Number ", font=fnt)
        lab1.place(x=20, y=60)
        tex1 = Entry(base5, font=fnt)
        tex1.place(x=250, y=60)
        bt1 = Button(base5, text="Delete", font=fnt, command=delete)
        bt1.place(x=200, y=110)
        bt2 = Button(base5, text="Back", font=fnt, command=Back)
        bt2.place(x=280, y=110)
        base.destroy()
        base5.mainloop()

    def Event4():
        def leave():
            a = str(tex1.get())
            b = str(tex2.get())
            c = str(tex3.get())
            d = str(tex4.get())
            e = str(tex5.get())
            f = str(tex6.get())
            g = str(tex7.get())
            h = str(tex8.get())
            con = sqlite3.connect("hostel.db")
            q = "insert into leave_girl('" + a +  ",'" + d + "'," + e + ",'" + f + "'," + g + ",'" + h + "')"
            con.execute(q)
            con.commit()
            con.close()
            print("Succefully inserted....!!")
            messagebox.showinfo("SAVED", "Data  Saved  sucessfully...")
            print("data SAved")

        def BACK():
            base4.destroy()
            base.mainloop()

        base4 = Tk()
        base4.geometry("800x700")
        base4.title("Add New Girl ")
        fnt = ("Arial", 16)

        lab1 = Label(base4, text="Enter Name  ", font=fnt)
        lab1.place(x=20, y=60)
        tex1 = Entry(base4, font=fnt)
        tex1.place(x=250, y=60)

        lab2 = Label(base4, text="Roll Number ", font=fnt)
        lab2.place(x=20, y=100)
        tex2 = Entry(base4, font=fnt)
        tex2.place(x=250, y=100)

        lab3 = Label(base4, text="Room Number", font=fnt)
        lab3.place(x=20, y=140)
        tex3 = Entry(base4, font=fnt)
        tex3.place(x=250, y=140)

        lab4 = Label(base4, text="reason to leave", font=fnt)
        lab4.place(x=20, y=180)
        tex4 = Entry(base4, font=fnt)
        tex4.place(x=250, y=180)

        lab5 = Label(base4, text="how many day on leave  ", font=fnt)
        lab5.place(x=20, y=220)
        tex5 = Entry(base4, font=fnt)
        tex5.place(x=250, y=220)

        lab6 = Label(base4, text="relative name ", font=fnt)
        lab6.place(x=20, y=260)
        tex6 = Entry(base4, font=fnt)
        tex6.place(x=250, y=260)

        lab7 = Label(base4, text=" realtive moblie number ", font=fnt)
        lab7.place(x=20, y=300)
        tex7 = Entry(base4, font=fnt)
        tex7.place(x=250, y=300)

        lab8 = Label(base4, text=" realtive address ", font=fnt)
        lab8.place(x=20, y=340)
        tex8 = Entry(base4, font=fnt)
        tex8.place(x=250, y=340)
        bt1 = Button(base4, text="submit", font=fnt, command=leave)
        bt1.place(x=200, y=480)
        bt2 = Button(base4, text="BACK", font=fnt, command=BACK)
        bt2.place(x=400, y=480)

        base.destroy()
        base4.mainloop()

    def Visitor():
        def visitor():
            a = str(tex1.get())
            b = str(tex2.get())
            c = str(tex3.get())
            d = str(tex4.get())
            con = sqlite3.connect("hostel.db")
            q = "insert into visitior values('" + a + "','" + b + "','" + c + "','" + d + "')"
            con.execute(q)
            con.commit()
            con.close()
            print("Succefully inserted....!!")
            messagebox.showinfo("SAVED", "Data  Saved  sucessfully...")
            print("data SAved")

        def back():
            base3.destroy()
            Login()
            base.mainloop()

        base3 = Tk()
        base3.geometry("800x700")
        base3.title("Visitor list")
        fnt = ("Arial", 16)

        lab1 = Label(base3, text="Visitor Name  ", font=fnt)
        lab1.place(x=20, y=60)
        tex1 = Entry(base3, font=fnt)
        tex1.place(x=250, y=60)

        lab2 = Label(base3, text=" Visit to  ", font=fnt)
        lab2.place(x=20, y=100)
        tex2 = Entry(base3, font=fnt)
        tex2.place(x=250, y=100)

        lab3 = Label(base3, text="Relation", font=fnt)
        lab3.place(x=20, y=140)
        tex3 = Entry(base3, font=fnt)
        tex3.place(x=250, y=140)

        lab4 = Label(base3, text="Date", font=fnt)
        lab4.place(x=20, y=180)
        tex4 = Entry(base3, font=fnt)
        tex4.place(x=250, y=180)

        bt4 = Button(base3, text="Save Date", font=fnt, command=visitor)
        bt4.place(x=210, y=240)

        bt2 = Button(base3, text="BACK", font=fnt, command=back)
        bt2.place(x=350, y=240)

        base3.mainloop()


    def SearchGirl():
        def Fetch():
            a = str(tex1.get())
            q = "Select sc_roll,s_name,s_coll,s_year,s_mob,sp_mob,s_age,s_village,s_fees,admis_date  from girls where sh_roll= " + a
            con = sqlite3.connect("hostel.db")
            cur = con.cursor()
            b = list(cur.execute(q))
            clg_r = b[0][0]
            s_n = b[0][1]
            s_c = b[0][2]
            class1 = b[0][3]
            s_no = b[0][4]
            sp_no = b[0][5]
            s_age = b[0][6]
            s_v = b[0][7]
            fees = b[0][8]
            addate = b[0][9]
            print("college Roll No : ", b[0][0])
            print("Student Name    :", b[0][1])
            print("Student college :", b[0][2])
            print("Class           :", b[0][3])
            print("Student Mobile  :", b[0][4])
            print("Parents Mobile  :", b[0][5])
            print("Student Age     :", b[0][6])
            print("Stuent Village  : ", b[0][7])
            print("Fees Payed      :", b[0][8])
            print("Adimisstion date: ", b[0][9])
            print("\n\n\n\n\n\n\n")

            result = Tk()
            result.geometry("800x700")
            result.title("Data Found ")
            fnt = ("Arial", 14)

            lab2 = Label(result, text="College Roll Number ", font=fnt)
            lab2.place(x=20, y=100)
            tex2 = Entry(result, font=fnt)
            tex2.place(x=250, y=100)
            tex2.insert(0, clg_r)

            lab3 = Label(result, text="Name", font=fnt)
            lab3.place(x=20, y=140)
            tex3 = Entry(result, font=fnt)
            tex3.place(x=250, y=140)
            tex3.insert(0, s_n)

            lab4 = Label(result, text="College Name", font=fnt)
            lab4.place(x=20, y=180)
            tex4 = Entry(result, font=fnt)
            tex4.place(x=250, y=180)
            tex4.insert(0, s_c)

            lab5 = Label(result, text="Year of Studing ", font=fnt)
            lab5.place(x=20, y=220)
            tex5 = Entry(result, font=fnt)
            tex5.place(x=250, y=220)
            tex5.insert(0, class1)

            lab6 = Label(result, text="Mobile Number ", font=fnt)
            lab6.place(x=20, y=260)
            tex6 = Entry(result, font=fnt)
            tex6.place(x=250, y=260)
            tex6.insert(0, s_no)

            lab7 = Label(result, text=" Parent Mobile Number ", font=fnt)
            lab7.place(x=20, y=300)
            tex7 = Entry(result, font=fnt)
            tex7.place(x=250, y=300)
            tex7.insert(0, sp_no)

            lab8 = Label(result, text=" Age ", font=fnt)
            lab8.place(x=20, y=340)
            tex8 = Entry(result, font=fnt)
            tex8.place(x=250, y=340)
            tex8.insert(0, s_age)

            lab9 = Label(result, text=" Village ", font=fnt)
            lab9.place(x=20, y=380)
            tex9 = Entry(result, font=fnt)
            tex9.place(x=250, y=380)
            tex9.insert(0, s_v)

            lab10 = Label(result, text="Fees Paid", font=fnt)
            lab10.place(x=20, y=420)
            tex10 = Entry(result, font=fnt)
            tex10.place(x=250, y=420)
            tex10.insert(0, fees)

            lab11 = Label(result, text="Admission Date", font=fnt)
            lab11.place(x=20, y=460)
            tex11 = Entry(result, font=fnt)
            tex11.place(x=250, y=460)
            tex11.insert(0, addate)
            result.mainloop()
            con.commit()

        def Back():
            base2.destroy()
            Login()
            base.mainloop()

        base2 = Tk()
        base2.geometry("800x700")
        base2.title("Add New Girl ")
        fnt = ("Arial", 16)
        lab1 = Label(base2, text="Enter Hostel Roll Number ", font=fnt)
        lab1.place(x=20, y=60)
        tex1 = Entry(base2, font=fnt)
        tex1.place(x=250, y=60)
        bt1 = Button(base2, text="Serch", font=fnt, command=Fetch)
        bt1.place(x=200, y=110)
        bt2 = Button(base2, text="Back", font=fnt, command=Back)
        bt2.place(x=280, y=110)
        base.destroy()
        base2.mainloop()

    def Event1():
        def Savedata():
            a = str(tex1.get())
            b = str(tex2.get())
            c = str(tex3.get())
            d = str(tex4.get())
            e = str(tex5.get())
            f = str(tex6.get())
            g = str(tex7.get())
            h = str(tex8.get())
            i = str(tex9.get())
            j = str(tex10.get())
            date = str(datetime.date.today())

            con = sqlite3.connect("hostel.db")
            q = "insert into girls values(" + a + "," + b + ",'" + c + "','" + d + "','" + e + "'," + f + "," + g + "," + h + ",'" + i + "'," + j + ",'" + date + "')"
            con.execute(q)
            con.commit()
            con.close()
            print("Succefully inserted....!!")
            messagebox.showinfo("SAVED", "Data  Saved  sucessfully...")
            print("data SAved")

        def BACK():
            base1.destroy()
            base.mainloop()

        base1 = Tk()
        base1.geometry("800x700")
        base1.title("Add New Girl ")
        fnt = ("Arial", 16)
        lab1 = Label(base1, text="Enter Hostel Roll no ", font=fnt)
        lab1.place(x=20, y=60)
        tex1 = Entry(base1, font=fnt)
        tex1.place(x=250, y=60)

        lab2 = Label(base1, text="College Roll Number ", font=fnt)
        lab2.place(x=20, y=100)
        tex2 = Entry(base1, font=fnt)
        tex2.place(x=250, y=100)

        lab3 = Label(base1, text="Name", font=fnt)
        lab3.place(x=20, y=140)
        tex3 = Entry(base1, font=fnt)
        tex3.place(x=250, y=140)

        lab4 = Label(base1, text="College Name", font=fnt)
        lab4.place(x=20, y=180)
        tex4 = Entry(base1, font=fnt)
        tex4.place(x=250, y=180)

        lab5 = Label(base1, text="Year of Studing ", font=fnt)
        lab5.place(x=20, y=220)
        tex5 = Entry(base1, font=fnt)
        tex5.place(x=250, y=220)

        lab6 = Label(base1, text="Mobile Number ", font=fnt)
        lab6.place(x=20, y=260)
        tex6 = Entry(base1, font=fnt)
        tex6.place(x=250, y=260)

        lab7 = Label(base1, text=" Parent Mobile Number ", font=fnt)
        lab7.place(x=20, y=300)
        tex7 = Entry(base1, font=fnt)
        tex7.place(x=250, y=300)

        lab8 = Label(base1, text=" Age ", font=fnt)
        lab8.place(x=20, y=340)
        tex8 = Entry(base1, font=fnt)
        tex8.place(x=250, y=340)

        lab9 = Label(base1, text=" Village ", font=fnt)
        lab9.place(x=20, y=380)
        tex9 = Entry(base1, font=fnt)
        tex9.place(x=250, y=380)

        lab10 = Label(base1, text="Fees Paid", font=fnt)
        lab10.place(x=20, y=420)
        tex10 = Entry(base1, font=fnt)
        tex10.place(x=250, y=420)

        lab11 = Label(base1, text="Admission Date", font=fnt)
        lab11.place(x=20, y=460)
        tex11 = Entry(base1, font=fnt)
        tex11.place(x=250, y=460)

        bt1 = Button(base1, text="ADD", font=fnt, command=Savedata)
        bt1.place(x=200, y=580)
        bt2 = Button(base1, text="BACK", font=fnt, command=BACK)
        bt2.place(x=400, y=580)

        base1.mainloop()

    def BACK():
        base.destroy()
        base.mainloop()
    lab1 = Label(base, text="1", font=fnt)
    lab1.place(x=20, y=60)
    bt1 = Button(base, text="Add New Girl", font=fnt, command=Event1)
    bt1.place(x=100, y=50)

    lab2 = Label(base, text=2, font=fnt)
    lab2.place(x=20, y=160)
    bt2 = Button(base, text="Search Girl", font=fnt, command=SearchGirl)
    bt2.place(x=100, y=150)

    lab3 = Label(base, text=3, font=fnt)
    lab3.place(x=20, y=260)
    bt3 = Button(base, text="Visitor", font=fnt, command=Visitor)
    bt3.place(x=100, y=250)

    lab5 = Label(base, text="5", font=fnt)
    lab5.place(x=20, y=360)
    bt5 = Button(base, text="Delete Info", font=fnt, command=Del_Info)
    bt5.place(x=100, y=350)

    bt6 = Button(base, text="BACK", font=fnt, command=BACK)
    bt6.place(x=400, y=480)

    base.mainloop()
def Logout():
    print("Logout Sucessfully...")
def Signup():
    def sign():
        a = str(tex1.get())
        b = str(tex2.get())
        c = str(tex3.get())
        con = sqlite3.connect("hostel.db")
        q = "insert into admin values('" + a + "','" + b + "','" + c + "')"
        con.execute(q)
        con.commit()
        con.close()
        print("Succefully inserted....!!")
        messagebox.showinfo("SAVED", "Profile Created sucessfully...")
        print("data Saved")

    def back():
        singup.destroy()
        base1.mainloop()

    singup = Tk()
    singup.geometry("800x700")
    singup.title("ADMIN SIGNUP ")
    fnt = ("Arial", 14)

    lab1 = Label(singup, text="ADMIN NAME  ", font=fnt)
    lab1.place(x=20, y=60)
    tex1 = Entry(singup, font=fnt)
    tex1.place(x=250, y=60)

    lab2 = Label(singup, text="EMAIL", font=fnt)
    lab2.place(x=20, y=100)
    tex2 = Entry(singup, font=fnt)
    tex2.place(x=250, y=100)

    lab3 = Label(singup, text="PASSWORD", font=fnt)
    lab3.place(x=20, y=140)
    tex3 = Entry(singup,show = "*", font=fnt)
    tex3.place(x=250, y=140)

    bt4 = Button(singup, text="Create", font=fnt, command=sign)
    bt4.place(x=210, y=240)

    bt2 = Button(singup, text="BACK", font=fnt, command=back)
    bt2.place(x=350, y=240)
    singup.mainloop


def FetchAd():
    a1 = str(inputBox.get())
    a2 = str(inputBox1.get())

    con = sqlite3.connect("hostel.db")
    q = "Select * from admin"
    cur = con.cursor()
    ad = list(cur.execute(q))
    ad_n = ad[0][0]
    ad_email = ad[0][1]
    ad_pass = ad[0][2]

    if ad == None:
        messagebox.showinfo("Please Signup","CREATE ADMIN")
    else:
        if ad_email == inputBox.get() and ad_pass == inputBox1.get():
            Login()
        else:
            messagebox.showinfo("INVALID LOGIN","please enter valid input !!!")


base1 = Tk()
base1.title("Login Form")
base1.geometry("1000x700")
base1.configure(bg="black")
header = Label(base1,text="Login ",font=50,height=4,fg='white',bg='black')
header.pack()

text1 = Label(base1,text="Enter Email or Phone: ",fg='white',bg='black')
text1.place(x = 350, y = 110)
inputBox = Entry(base1,font=20,border=0)
inputBox.place(x = 510,y = 110)

text2 = Label(base1,text="Enter Password: ",fg = "white",bg='black')
text2.place(x = 350, y = 150)
inputBox1 = Entry(base1,font=20,show = "*",border=0)
inputBox1.place(x = 510,y = 150)

btn = Button(base1,text = "Login",bg='#0d6efd',fg='white', command=FetchAd) #Login
btn.place(x = 360,y = 230,height=50,width=150)

btn = Button(base1,text = "Reset",bg='#198754',fg='white',command=remove)
btn.place(x = 540,y = 230,height=50,width=150)

btn5 = Button(base1,text = "New User?",fg='Black',command=Signup)
btn5.place(x = 480,y = 300,height=50,width=150)

base1.mainloop()