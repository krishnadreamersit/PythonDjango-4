from tkinter import *

# Creating Window
"""
frame = Tk()
frame.mainloop()
"""

# Setting Size
"""
frame = Tk()
frame.geometry("400x250")
frame.mainloop()
"""

# Fixed size (Non-resizable)
"""
frame = Tk()
frame.geometry("400x250")
frame.resizable(False, False)
frame.mainloop()
"""

# Task-13.1
    # Change system icon of Window
    # Change title of Window

"""
frame = Tk()
frame.title("My Window")
frame.geometry("400x250")
frame.resizable(False, False)
icon = PhotoImage(file="images/icon.png")
frame.iconphoto(False, icon)
frame.mainloop()
"""

# Task-13.2
    # Add Label
    # Add TextBox
    # Add Button

def print_hello():
    print("Hello")

frame = Tk()
frame.title("My Window")
frame.geometry("400x250")
frame.resizable(False, False)
icon = PhotoImage(file="images/icon.png")
frame.iconphoto(False, icon)

lbl_id = Label(frame, text="Enter ID : ")
lbl_id.place(x=10, y=10)

txt_id = Entry(frame, text="<ID>")
txt_id.place(x=75, y=10)

btn_close = Button(frame, text="Close", command=print_hello)
btn_close.place(x=75, y=50)

frame.mainloop()


