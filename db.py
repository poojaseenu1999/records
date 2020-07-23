from tkinter import *

app = Tk()
app.title('databse entry')




firstname = Entry(app,bg='white').grid(row=0,column=1)
lastname = Entry(app,bg='white').grid(row=2,column=1)
age = Entry(app,bg='white').grid(row=3,column=1)
city = Entry(app,bg='white').grid(row=4,column=1)
pincode = Entry(app,bg='white').grid(row=5,column=1)

app.mainloop()
