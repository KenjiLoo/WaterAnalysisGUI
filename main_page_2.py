from tkinter import *
from tkinter.ttk import *

# --------------------------------------TOP BAR---------------------------------------------------
# define window as GUI window, set minimum dimension
window = Tk()
window.minsize(850,450)
window.maxsize(1000, 550)

# empty space for arranging elements
empty = Label(window, text="                                                                                                         ")
empty.grid(row=0, column=0)

# top bar with logo
logo = PhotoImage(file = "Assets/Group 2.png")
title_logo = Label(window, text="", image=logo, compound=CENTER)
title_logo.grid(row=0, column=1)

# empty space between title logo and the app logo
empty2 = Label(window, text="                                                                          ")
empty2.grid(row=0, column=2)

# top bar right side logo
logo2 = PhotoImage(file = "Assets/logo 2.png")
right_logo = Label(window, text="", image=logo2, compound=CENTER)
right_logo.grid(row=0, column=3)

# --------------------------------------MAIN BUTTONS---------------------------------------------------
# button 1
button1_image = PhotoImage(file = "Assets/button1_2.png")
button1 = Button(window, image=button1_image)
button1.grid(row=1, column=0)

# button 2
button2_image = PhotoImage(file = "Assets/button2_2.png")
button2 = Button(window, text="ID: 2020218", compound=TOP, image=button2_image)
button2.grid(row=1, column=1)

# button 3
button3_image = PhotoImage(file = "Assets/button3_2.png")
button3 = Button(window, image=button3_image)
button3.grid(row=1, column=2)

# --------------------------------------3rd ROW BUTTONS---------------------------------------------------
# empty space as row 3, 4, 5
empty3 = Label(window, text=" ")
empty3.grid(row=3, column=0)
empty4 = Label(window, text=" ")
empty4.grid(row=4, column=0)
empty5 = Label(window, text=" ")
empty5.grid(row=5, column=0)

# button 4
button4_image = PhotoImage(file = "Assets/button4_2.png")
button4 = Button(window, image=button4_image)
button4.grid(row=4, column=1)

# to run the window
window.mainloop()
