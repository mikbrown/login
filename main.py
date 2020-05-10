#import modules

from tkinter import *
import tkinter as tk
import tkinter.filedialog
import os
import sqlite3

# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen) #Frame derived from main GUI
    register_screen.title("Register")
    register_screen.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar() #text entry box
    password = StringVar()
    Label(register_screen, text="Fill in your information below", width="300", bg="yellow").pack()
    Label(register_screen, text="").pack()
    Label(register_screen, text="Username: ").pack()
    username_entry = Entry(register_screen, textvariable=username) #set username entry
    username_entry.pack()
    Label(register_screen, text="Password: ").pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="red", command = register_user).pack()


# Designing window for login 

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Fill in your information below", width="300", bg="yellow").pack()
    Label(login_screen, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_login_entry
    global password_login_entry
    Label(login_screen, text="Username: ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password: ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", bg = "red", width=10, height=1, command = login_verify).pack()

# Implementing event on register button

def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w") #open file under username in write mode
    file.write(username_info + "\n")#write username into file
    file.write(password_info)
    file.close()

    username_entry.delete(0, END) #ability to delete text
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button 

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognized()

    else:
        user_not_found()

#function to open drop down selection  

def openFile():
    f = tkinter.filedialog.askopenfilename(
    parent=login_success_screen, initialdir='C:/Users/keera/OneDrive/Documents/csv',
    title='Choose dataset'
    )
    print(f)
    text2 = open(f).read()
    print(text2)
    




# Designing popup for login success

def login_sucess():
    N1 = ["Covid-19 Data", ]
    N2 = ["Covid-19 Line List Data"]
    N3 = ["Covid-19 Open Line List Data"]
    N4 = ["Covid-19 Confirmed Cases Data"]
    N5 = ["Covid-19 Confirmed US Cases Data"]
    N6 = ["Covid-19 Deaths Data"]
    N7 = ["Covid-19 US Deaths Data"]
    N8 = ["Covid-19 Recovered Cases Data"]
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Covid-19 Query")
    login_success_screen.geometry("300x250")
    global query
    query = StringVar(login_success_screen)
    Label(login_success_screen, text="Pick your desired dataset to view", width="300", bg="yellow").pack()
    Label(login_success_screen, text="").pack()
    Label(login_success_screen, text="Queries: ").pack()
    set1 = OptionMenu(login_success_screen, query, N1, N2, N3, N4, N5, N6, N7, N8)
    set1.configure(width = 90, font=("Calibri", 10))
    set1.pack()
    Button(login_success_screen, text="OK", command=openFile).pack()
    login_success_screen.mainloop()
    
    
    
 
	
# Designing popup for login invalid password

def password_not_recognized():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognized).pack()

# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognized():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


#Connecting to sqllite
conn = sqlite3.connect('covid.db')
c = conn.cursor()
conn.commit()
conn.close()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk() #create GUI
    main_screen.geometry("300x250") #scale of GUI
    main_screen.title("Account Login")
    Label(text="Pick An Option:", bg="yellow", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", bg="red", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", bg="red", height="2", width="30", command = register).pack()

    main_screen.mainloop() #start the GUI


main_account_screen()