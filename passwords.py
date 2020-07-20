from tkinter import *
from tkinter import messagebox



#password window

class password():
    def __init__(self):
        self.root=Tk()
        self.pass_label = Label(self.root,text="password", font=('Arial', 14))
        self.e=Entry(self.root, font=('Arial', 14))
        self.sub=Button(self.root,text='verify', font=('Arial', 14),bg="white",command=self.check)
        self. pass_label.pack()
        self.e.pack(pady=10)
        self.sub.pack()
        
       
        self.root.mainloop()
    
        
    def check(self):
      self.value = self.e.get()
      # print(self.value)
      if "sha" == self.value:

        self.root.destroy()
        def text_file():
           #create a file named text
           f=open('text.txt','a')
           f.close()

           with open('text.txt','r') as f :
                decrypt=""
                
                while 1: 
      
                  # read by character 
                  char = f.read(1)           
                  if not char:  
                      break
                        
                  else:
                     #decrypting to windo
                          if char == ' ':
                            decrypt += ' '
                          else:
                            decrypt += chr(ord(char) + 4)
                y = decrypt.split()
                for q in y:
                    
                          global i
                          mylabel=Label(window,text=q,font=('Times', 13))
                          mylabel.grid(row=i , columnspan =3)
                          i+=1
        
#user window

        global i
        i = 4

        def store():
            name = site_e.get()
            site_e.delete(0,'end')
            pas=password_e.get()
            password_e.delete(0,'end')

            #encrypting to file
            encry=''
            encrypt=''
            for letter in pas:
                    if letter == ' ':
                       encrypt += ' '
                    else:
                       encrypt += chr(ord(letter) - 4)
            for letter in name:
                    if letter == ' ':
                       encry += ' '
                    else:
                       encry += chr(ord(letter) - 4)
            a=""
            for letter in " site:-":
                    if letter == ' ':
                       a += ' '
                    else:
                       a += chr(ord(letter) - 4)
            b=""
            for letter in "--password:-":
                    if letter == ' ':
                       b += ' '
                    else:
                       b += chr(ord(letter) - 4)
            
            with open('text.txt','a') as f :
               f.write(a+encry+b + encrypt)
            
            if True:
                global i
                mylabel=Label(window,text=" site:-"+name+'--'+ "password:-" + pas,font=('Times', 13))
                mylabel.grid(row=i , columnspan =3)
                i+=1 

        window= Tk()
        window.title(' my accouts')
        window.geometry('500x500')
        site= Label(window, text='site',font=('Times', 18))
        site_e= Entry(window,font=('Times', 18),width = 30,borderwidth=10)
        password= Label(window, text='password',font=('Times', 18))
        password_e= Entry(window, font=('Times', 18),width = 30,borderwidth=10)
        submit=Button(window, text='submit',font=('Times', 18),command=store)

        text_file()

        site.grid(row=0,column=0,sticky= W)
        password.grid(row=1,column=0,sticky= E)
        site_e.grid(row=0,column=1)
        password_e.grid(row=1,column=1)
        submit.grid(row=2,column=1,padx=30,sticky= S,pady =15)


        window.mainloop()
      else:
        messagebox.showinfo(' wrong password ')

    
      
      
p=password()





