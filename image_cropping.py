from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2


#-- FUNCTION DEFINITION --#
def homePage(tk):
    tk.destroy()
    import camera
    #take note: may return to main_page_2

def finalPage(tk):
    tk.destroy()
    import time_setting


# --------------------------------------TOP BAR---------------------------------------------------
# define window as GUI window, set minimum dimension
window = Tk()
window.title("Water Analysis Grp9A")
window.minsize(500,450)
window.configure(bg="white")
style = ttk.Style()
style.configure("BW.TLabel", background="white")

# set blue bar
blue_bar_image = PhotoImage(file = "Assets/blue_bar.png")
blue_bar = Button(window, text="< Homepage",
                  compound=RIGHT,
                  image=blue_bar_image,
                  background="#81D3F9",
                  activeforeground="white",
                  activebackground="white",
                  borderwidth=0,
                  font=("IBM Plex Sans", 10),
                  command=lambda : homePage(window))
blue_bar.pack(fill=BOTH)

# --------------------------------------CAMERA FRAME---------------------------------------------------
# insert empty space
empty = Label(window, text="", background="white")
empty.pack()

empty2 = Label(window, text="                                           ", background="white")
empty2.pack()


camera_frame_image = PhotoImage(file = "Assets/cameraframe.png")
camera_frame = Label(window,
                     image=camera_frame_image,
                     background="white")
camera_frame.pack()

save_button_image = PhotoImage(file = "Assets/save_button.png")
save_button = Button(window,
                        image=save_button_image,
                        background="white",
                        activeforeground="white",
                        activebackground="white",
                        borderwidth=0,
                        command=lambda : finalPage(window))
save_button.pack()

# to run the window
window.mainloop()

