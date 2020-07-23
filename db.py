from tkinter import *

app = Tk()
app.title('databse entry')




firstname = Entry(app,bg='white').grid(row=0,column=1)
lastname = Entry(app,bg='white').grid(row=2,column=1)
age = Entry(app,bg='white').grid(row=3,column=1)
city = Entry(app,bg='white').grid(row=4,column=1)
pincode = Entry(app,bg='white').grid(row=5,column=1)

firstname1 = Label(app,bg='white',text ='firstname').grid(row=0,column=0)
lastname1 = Label(app,bg='white',text ='lastname').grid(row=2,column=0)
age1 = Label(app,bg='white',text ='age').grid(row=3,column=0)
city1 = Label(app,bg='white',text ='city').grid(row=4,column=0)
pincode1 = Label(app,bg='white',text ='pincode').grid(row=5,column=0)

app.mainloop()
