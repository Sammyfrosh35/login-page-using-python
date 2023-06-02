from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class login:
     def __init__(self, root):
        self.root = root
        self.root.title("login page")
        self.root.geometry('1199x600+100+50')
        self.root.resizable(False, False)
 
        def submit_function():
            if self.Username.get()=="" or self.Password.get()=="":
                messagebox.showerror("error",'All feilds are required',parent=self.root)
            
            elif self.Username.get()!="Samtech" or self.Password.get()!="1234":
                messagebox.showerror("error",'Invalid Username or Password',parent=self.root)
            
            
            else: 
                messagebox.showinfo("Welcome",f"welcome {self.Username.get()}")


        def forgot_function():
           messagebox.showinfo("Error", "As old as you are, you dey forget password idiot!")


        # background image
        self.bg=ImageTk.PhotoImage(file="IMAGES/3.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)


        #login frame
        Frame_login = Frame(self.root, bg='white')
        Frame_login.place(x=330, y=150, width=550, height=400)


        #title and subtitle
        title= Label(Frame_login, text='Login here', font=('sans serif', 35, 'bold'), fg="#6162FF", bg="white").place(x=90, y=30)

        Username= Label(Frame_login, text='Username', font=('Goudy old style', 14, 'bold'), fg="grey", bg="white").place(x=90, y=140)
        self.Username= Entry(Frame_login, bg="#E7E6E6")
        self.Username.place(x=90,  y=170, width=320, height=35)
        
        #password 
        Password= Label(Frame_login, text='Password', font=('Goudy old style', 14, 'bold'), fg="grey", bg="white").place(x=90, y=210)
        self.Password= Entry(Frame_login, bg="#E7E6E6")
        self.Password.place(x=90,  y=240, width=320, height=35)

        #button
        forget=Button(Frame_login, text='Forgot Password?', command=forgot_function, cursor="hand2", font=('Goudy old style', 12),  fg="#6162FF", bg="white").place(x=90, y=280)
        
        #login
        Login=Button(Frame_login, command= submit_function, cursor="hand2" , text='Login',border=0, font=('Goudy old style', 15, "bold"),  fg="white", bg="#6162FF").place(x=90, y=320,  width=180, height= 40)

        
      


 

root = Tk()
object = login(root) 
root.mainloop()

 