from tkinter import *
from tkinter import ttk

#-- FUNCTION DEFINITION --#
def homePage(tk):
    tk.destroy()
    import main_page
    #take note: may return to main_page_2

def finalPage(tk):
    tk.destroy()
    import final_page

# --------------------------------------TOP BAR---------------------------------------------------
# define window as GUI window, set minimum dimension
window = Tk()
window.minsize(850,450)
window.maxsize(1000, 550)
window.configure(bg="white")
style = ttk.Style()
style.configure("BW.TLabel", background="white")

# set blue bar
blue_bar_image = PhotoImage(file = "Assets/blue_bar.png")
blue_bar = Button(window, text="<Homepage",
                  compound=RIGHT,
                  image=blue_bar_image,
                  background="white",
                  activeforeground="white",
                  activebackground="white",
                  borderwidth=0,
                  command=lambda : homePage(window))
blue_bar.grid(row=0, columnspan=3)

# --------------------------------------CAMERA FRAME---------------------------------------------------
# insert empty space
empty = Label(window, text="", background="white")
empty.grid(row=1, column=0)

empty2 = Label(window, text="                                           ", background="white")
empty2.grid(row=1, column=2)

# insert camera frame
camera_frame_image = PhotoImage(file = "Assets/cameraframe.png")
camera_frame = Label(window,
                     image=camera_frame_image,
                     background="white")
camera_frame.grid(row=1, column=1)

# --------------------------------------CAMERA FRAME---------------------------------------------------
# insert camera capture button
camera_capture_image = PhotoImage(file = "Assets/camera_capture.png")
camera_capture = Button(window,
                        image=camera_capture_image,
                        background="white",
                        activeforeground="white",
                        activebackground="white",
                        borderwidth=0,
                        command=lambda : finalPage(window))
camera_capture.grid(row=2, column=1)

# to run the window
window.mainloop()

