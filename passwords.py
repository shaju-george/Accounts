from tkinter import *

window= Tk()

window.title(' my accouts')
window.geometry('500x500')

def store():
    name = site_e.get()
    site_e.delete(0,'end')
    pas=password_e.get()
    password_e.delete(0,'end')
    mylabel=Label(window,text=" site :"+name + " password :" + pas,font=('Times', 18))
    mylabel.grid(row=4 , columnspan =3)

site= Label(window, text='site',font=('Times', 18))
site_e= Entry(window,font=('Times', 18),width = 30,borderwidth=10)
password= Label(window, text='password',font=('Times', 18))
password_e= Entry(window, font=('Times', 18),width = 30,borderwidth=10)
submit=Button(window, text='submit',font=('Times', 18),command=store)

site.grid(row=0,column=0,sticky= W)
password.grid(row=1,column=0,sticky= E)
site_e.grid(row=0,column=1)
password_e.grid(row=1,column=1)
submit.grid(row=2,column=1,padx=30,sticky= S,pady =15)


window.mainloop()