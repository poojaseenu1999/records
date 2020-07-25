from tkinter import *
import sqlite3

app = Tk()
app.title('databse entry')


# conn=sqlite3.connect("python1.db")
# cur=conn.cursor()
# cur.execute("CREATE TABLE  student (firstname TEXT,lastname TEXT,age integer,city TEXT,pincode NUMBER) ")


def submit():

    f_name.delete(0,END)
    l_name.delete(0,END)
    age.delete(0,END)
    city.delete(0,END)
    pincode.delete(0,END)





f_name = Entry(app,bg='light pink').grid(row=0,column=1)
l_name = Entry(app,bg='light pink').grid(row=2,column=1)
age = Entry(app,bg='light pink').grid(row=3,column=1)
city = Entry(app,bg='light pink').grid(row=4,column=1)
pincode = Entry(app,bg='light pink').grid(row=5,column=1)

firstname1 = Label(app,bg='white',text ='firstname',fg = 'blue').grid(row=0,column=0)
lastname1 = Label(app,bg='white',text ='lastname',fg = 'blue').grid(row=2,column=0)
age1 = Label(app,bg='white',text ='age',fg = 'blue').grid(row=3,column=0)
city1 = Label(app,bg='white',text ='city',fg = 'blue').grid(row=4,column=0)
pincode1 = Label(app,bg='white',text ='pincode',fg = 'blue').grid(row=5,column=0)

but1=Button(app,text='add entry to database',command=submit).grid(row=6,column=1)
but2=Button(app,text='list the entry').grid(row=7,column=1)

# conn.commit()
# conn.close()

app.mainloop()
