from tkinter import *
import sqlite3

# conn=sqlite3.connect("python.db")
# cur=conn.cursor()
# cur.execute("CREATE TABLE  database (firstname TEXT,lastname TEXT,address TEXT,coty TEXT,state TEXT,pincode NUMBER) ")
# conn.commit()
# conn.close()

def submit():
    conn=sqlite3.connect("python.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO database VALUES(:f_name, :l_name, :address, :city, :state, :pincode)")
    {
      'f_name':f_name.get(),
      'l_name':l_name.get(),
      'address':address.get(),
      'city':city.get(),
      'pincode':pincode.get()
     }
    conn.commit()
    conn.close()


app = Tk()
app.title('databse entry')




firstname = Entry(app,bg='light pink').grid(row=0,column=1)
lastname = Entry(app,bg='light pink').grid(row=2,column=1)
age = Entry(app,bg='light pink').grid(row=3,column=1)
city = Entry(app,bg='light pink').grid(row=4,column=1)
pincode = Entry(app,bg='light pink').grid(row=5,column=1)

firstname1 = Label(app,bg='white',text ='firstname',fg = 'blue').grid(row=0,column=0)
lastname1 = Label(app,bg='white',text ='lastname',fg = 'blue').grid(row=2,column=0)
age1 = Label(app,bg='white',text ='age',fg = 'blue').grid(row=3,column=0)
city1 = Label(app,bg='white',text ='city',fg = 'blue').grid(row=4,column=0)
pincode1 = Label(app,bg='white',text ='pincode',fg = 'blue').grid(row=5,column=0)

but1=Button(app,text='add entry to database').grid(row=6,column=1)
but2=Button(app,text='list the entry').grid(row=7,column=1)


app.mainloop()
