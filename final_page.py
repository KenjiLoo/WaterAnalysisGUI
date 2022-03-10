from tkinter import *
from tkinter.ttk import *

# --------------------------------------TOP BAR---------------------------------------------------
# define window as GUI window, set minimum dimension
window = Tk()
window.minsize(850,450)
window.maxsize(1000, 550)

# set blue bar
blue_bar_image = PhotoImage(file = "Assets/blue_bar.png")
blue_bar = Button(window, text="<Retake", compound=RIGHT, image=blue_bar_image)
blue_bar.grid(row=0, columnspan=3)

# --------------------------------------WORDS---------------------------------------------------
# success wording
success_image = PhotoImage(file = "Assets/success_wording.png")
success = Label(window, image=success_image)
success.grid(row=1, column=0)

# id display
id = Label(window, text="ID: 20202143", compound=CENTER, font=("Arial", 20))
id.grid(row=2, column=0)

# --------------------------------------BUTTONS---------------------------------------------------
# empty space
empty = Label(window, text="")
empty.grid(row=3)
empty2 = Label(window, text="")
empty2.grid(row=4)
empty3 = Label(window, text="")
empty3.grid(row=5)

# button 1
button1_image = PhotoImage(file = "Assets/button1_4.png")
button1 = Button(window, image=button1_image)
button1.grid(row=6, column=0)

# button 2
button2_image = PhotoImage(file = "Assets/button2_4.png")
button2 = Button(window, image=button2_image)
button2.grid(row=6, column=1)

# to run the window
window.mainloop()
