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
window.title("Water Analysis Grp9A")
window.maxsize(window, )
window.configure(bg="white")
style = ttk.Style()
style.configure("BW.TLabel", background="white")

# set blue bar
blue_bar_image = PhotoImage(file = "Assets/blue_bar.png")
blue_bar = Button(window, text="<Homepage",
                  compound=RIGHT,
                  image=blue_bar_image,
                  background="#81D3F9",
                  activeforeground="white",
                  activebackground="white",
                  borderwidth=0,
                  command=lambda : homePage(window))
blue_bar.pack(fill=BOTH)

# --------------------------------------CAMERA FRAME---------------------------------------------------
# insert empty space
empty = Label(window, text="", background="white")
empty.pack()

empty2 = Label(window, text="                                           ", background="white")
empty2.pack()

# insert camera frame
# Create a Label to capture the Video frames
label =Label(window)
label.pack()
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
   label.place(x=241, y=65, anchor='c')


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
camera_capture.pack()



# to run the window
window.mainloop()

