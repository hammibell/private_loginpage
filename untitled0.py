from tkinter import *
from tkinter import messagebox

root = Tk()

root.configure(background = "light yellow")
root.geometry("500x500")
root.title("Private Login Page")

heading = Label(root, text = "Register")
heading.place(relx = 0.5, rely = 0.2, anchor = CENTER)

username_label = Label(root, text = "Username: ")
username_label.place(relx = 0.35, rely = 0.35, anchor = CENTER)

password_label = Label(root, text = "Password: ")
password_label.place(relx = 0.35, rely = 0.45, anchor = CENTER)

username = Entry(root)
password = Entry(root)

username.place(relx = 0.6, rely = 0.35, anchor = CENTER)
password.place(relx = 0.6, rely = 0.45, anchor = CENTER)

global user
global pass1

user = username.get()
pass1 = password.get()


  

class private():
    
    def __init_(self, username, password):
        
        username = self.__username
        password = self.__password
        
    
            
    def sign_up(self, user, pass1):
        
            
        user = self.__user
        pass1 = self.__pass1
        
        
     
        
        print(user)
        print(pass1)

def openNewWindow():
    
    new_window = Tk()
        
    new_window.configure(background = "light green")
    new_window.geometry("500x500")
    new_window.title("Log In")
         
    heading1 = Label(new_window, text = "Log In")
    heading1.place(relx = 0.5, rely = 0.2, anchor = CENTER)
         
    username1_label = Label(new_window, text = "Username: ")
    username1_label.place(relx = 0.35, rely = 0.35, anchor = CENTER)
         
    password1_label = Label(new_window, text = "Password")
    password1_label.place(relx = 0.35, rely = 0.45, anchor = CENTER)
    
    same_username = Entry(new_window)
    same_password = Entry(new_window)

    same_username.place(relx = 0.6, rely = 0.35, anchor = CENTER)
    same_password.place(relx = 0.6, rely = 0.45, anchor = CENTER)
    
    user1 = same_username.get()
    pass2 = same_password.get()
    
    
    
    class confirm():
        
        def __init_(self, same_username, same_password, user1, pass2):
            
            same_username = self.__same_username
            same_password = self.__same_password
            

                
        def recocgnize(self, user1, pass2):
            
                
            user1 = self.__user1
            pass2 = self.__pass2
            
            user1 = same_username.get()
            pass2 = same_password.get()
            
                
    def validate(): 
        
        
        
        score = 0 
        

        
        if user == user1:
           
           score = score + 1
            
        if pass1 == pass2:
           score = score + 1
         
    def check():
        print(score)
        if score == 2:
            messagebox.showinfo("Alert", "Correct Username and Password!")
        
        else: 
            messagebox.showinfo("Alert", "Incorrect Username and Password! Try Again!")
        
        

    btn_validate = Button(new_window, text = "Validate", command = check)
    btn_validate.place(relx = 0.5, rely = 0.5, anchor = CENTER)
            
trial = private()

            
                 
       
sign_up_btn = Button(root, text = "Sign Up", command = openNewWindow)
sign_up_btn.place(relx = 0.5, rely = 0.55, anchor = CENTER)

root.mainloop()
        
        