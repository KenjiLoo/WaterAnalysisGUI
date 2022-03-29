from tkinter import *
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk
import cv2

#-- FUNCTION DEFINITION --#
def imageCroppingPage(tk):
    tk.destroy()
    import image_cropping

def finalPage(tk):
    webbrowser.open_new(r"https://www.google.com")
    tk.destroy()
    import final_page


# --------------------------------------TOP BAR---------------------------------------------------
# define window as GUI window, set minimum dimension
window = Tk()
window.title("Water Analysis Grp9A")
window.configure(bg="white")
window.minsize(855, 450)
style = ttk.Style()
style.configure("BW.TLabel", background="white")

# set blue bar
blue_bar_image = PhotoImage(file = "Assets/blue_bar.png")
blue_bar = Button(window, text="< Camera",
                  compound=RIGHT,
                  image=blue_bar_image,
                  background="#81D3F9",
                  activeforeground="white",
                  activebackground="white",
                  borderwidth=0,
                  font=("Poppins", 10),
                  command=lambda : imageCroppingPage(window))
blue_bar.pack(fill=BOTH)

#--------------------------------------SET TIME INTERVAL---------------------------------------------------

Label(window, text="", background="white").pack()
Label(window, text="TIME INTERVAL (minutes)", background="white",font=("Poppins", 10),).pack()
time_interval = Spinbox(window, from_=0, to=10)
time_interval.pack()
Label(window, text="", background="white").pack()
set_button_image = PhotoImage(file = "Assets/set_button.png")
set_button = Button(window,
                 image=set_button_image,
                 background="white",
                 borderwidth=0,
                 activeforeground="white",
                 activebackground="white",
                 font=("Poppins", 10),
                 command=lambda : finalPage(window))
set_button.pack()

# to run the window
window.mainloop()