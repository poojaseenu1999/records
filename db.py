from tkinter import *

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



app.mainloop()
