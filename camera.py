from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2


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
window.minsize(850,625)
window.maxsize(1000, 550)
window.title("Water Analysis Grp9A")
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
# Create a Label to capture the Video frames
label =Label(window)
label.grid(row=1, column=1)
cap= cv2.VideoCapture(0)

# Define function to show frame
def show_frames():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(20, show_frames)

show_frames()
# camera_frame_image = PhotoImage(file = "Assets/cameraframe.png")
# camera_frame = Label(window,
#                      image=camera_frame_image,
#                      background="white")
# camera_frame.grid(row=1, column=1)

# --------------------------------------CAMERA CAPTURE BUTTON---------------------------------------------------
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

