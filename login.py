import webbrowser
import mysql.connector
from subprocess import call
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#-- FUNCTION DEFINITION --#
def mainPage(tk):
    tk.destroy()
    import main_page

def callWeb():
    webbrowser.open_new(r"https://www.google.com")

# --------------------------------------TOP BAR---------------------------------------------------
# define window as GUI window, set minimum dimension
window = Tk()
window.minsize(500, 350)
window.maxsize(1000, 550)
window.title("Water Analysis Grp9A")
window.configure(bg="white")
style = ttk.Style()
style.configure("BW.TLabel", background="white")

# empty space for arranging elements
empty = Label(window,
              text="                                                                                             ",
              background="white")
empty.grid(row=0, column=0)

# top bar with logo
logo = PhotoImage(file="Assets/Group 2.png")
title_logo = Label(window,
                   text="",
                   image=logo,
                   compound=CENTER,
                   background="white")
title_logo.grid(row=0, column=1)

# empty space between title logo and the app logo
empty2 = Label(window, text="                                                                          ",
               background="white")
empty2.grid(row=0, column=2)

# top bar right side logo
logo2 = PhotoImage(file="Assets/logo 2.png")
right_logo = Label(window,
                   text="",
                   image=logo2,
                   compound=CENTER,
                   background="white")
right_logo.grid(row=0, column=3)

# --------------------------------------MAIN BUTTONS---------------------------------------------------
Label(window, text="Please enter login details",background="white",font=("Poppins", 10)).grid(row=1, column=1)
Label(window, text="",background="white").grid(row=2)
Label(window, text="Username",background="white",font=("Poppins", 10),).grid(row=3, column=1)
username_login_entry = Entry(window, textvariable="username")
username_login_entry.grid(row=4, column=1)
Label(window, text="",background="white").grid(row=5, column=1)
Label(window, text="Password",background="white",font=("Poppins", 10)).grid(row=6, column=1)
password__login_entry = Entry(window, textvariable="password", show= '*')
password__login_entry.grid(row=7, column=1)
Label(window, text="",background="white",font=("Poppins", 10)).grid(row=8, column=1)
login_button_image = PhotoImage(file = "Assets/login_button.png")
login_button = Button(window,
                 image=login_button_image,
                 background="white",
                 borderwidth=0,
                 activeforeground="white",
                 activebackground="white",
                 font=("Poppins", 10),
                 command=lambda : mainPage(window))
login_button.grid(row=9, column=1)
window.mainloop()

