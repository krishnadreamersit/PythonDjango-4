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
    # Add Event on Button Click
"""
def print_hello():
    print("Hello")

frame = Tk()
frame.title("My Window")
frame.geometry("400x250")
frame.resizable(False, False)
icon = PhotoImage(file="images/icon.png")
frame.iconphoto(False, icon)

# Label
lbl_id = Label(frame, text="Enter ID : ")
lbl_id.place(x=10, y=10)

# Single Line Text Box
txt_id = Entry(frame, text="<ID>")
txt_id.place(x=75, y=10)

# Push-Up Button
btn_close = Button(frame, text="Close", command=print_hello)
btn_close.place(x=75, y=50)

frame.mainloop()
"""

# Text (Text Area)
# Multiline Text
"""
frame = Tk()
frame.title("My Window")
frame.geometry("550x250")
frame.resizable(False, False)
icon = PhotoImage(file="images/icon.png")
frame.iconphoto(False, icon)

lbl_comment = Label(frame, text="Enter Comments : ")
lbl_comment.place(x=10, y=10)

# TextArea (Multi-Line Text Box)
txt_comment = Text(frame, height=5, width=40, bg='light green')
txt_comment.place(x=125, y=10)

frame.mainloop()
"""

# Radio Button
# Single selection from multiple options
"""
frame = Tk()
frame.title("My Window")
frame.geometry("400x250")
frame.resizable(False, False)
icon = PhotoImage(file="images/icon.png")
frame.iconphoto(False, icon)

# Label
lbl_gender = Label(frame, text="Select Gender : ")
lbl_gender.place(x=10, y=10)

# Radio Button
rb_male = Radiobutton(frame, text="Male")
rb_male.place(x=125, y=10)
rb_female = Radiobutton(frame, text="Female")
rb_female.place(x=200, y=10)

frame.mainloop()
"""

# Task 13.3
    # Radio button should be select only one at once
    # Read the value of selected radio button on button's click event


# CheckBox
# Select multiple options from multiple options
"""
frame = Tk()
frame.title("My Window")
frame.geometry("400x250")
frame.resizable(False, False)
icon = PhotoImage(file="images/icon.png")
frame.iconphoto(False, icon)

# Label
lbl_hobbies=Label(frame, text="Select Hobbies : ")
lbl_hobbies.place(x=10, y=10)

# Checkbutton (Checkbox)
chk_reading = Checkbutton(frame, text="Reading")
chk_reading.place(x=125, y=10)

chk_playing = Checkbutton(frame, text="Playing")
chk_playing.place(x=125, y=35)

frame.mainloop()
"""

# Listbox (Dropdown list)
"""
frame = Tk()
frame.title("My Window")
frame.geometry("400x250")
frame.resizable(False, False)
icon = PhotoImage(file="images/icon.png")
frame.iconphoto(False, icon)

# Listbox
lst_agegroup = Listbox(frame)
lst_agegroup.insert(0, '1')
lst_agegroup.insert(1, '2')
lst_agegroup.insert(2, '3')
lst_agegroup.insert(3, '4')
lst_agegroup.insert(4, '5')
lst_agegroup.insert(5, '6')
lst_agegroup.insert(6, '7')
lst_agegroup.insert(7, '8')
lst_agegroup.insert(8, '9')
lst_agegroup.insert(9, '10')
lst_agegroup.insert(10, '11')
lst_agegroup.insert(11, '12')
lst_agegroup.insert(12, '13')
lst_agegroup.insert(13, '14')
lst_agegroup.insert(14, '15')
lst_agegroup.place(x=10, y=10)

frame.mainloop()
"""

# Task 13.4
    # Customize list box with scrollbar (vertical)

# Task 13.5
    # Create combobox

# Create combobox
"""
from tkinter import ttk  # Combobox
frame = Tk()
frame.title("My Window")
frame.geometry("400x250")
frame.resizable(False, False)
icon = PhotoImage(file="images/icon.png")
frame.iconphoto(False, icon)

countries = ('India', 'China', 'Nepal', 'Bhutan', 'Pakistan')
country = ttk.Combobox(frame, width = 27)
country['values'] = countries;
country.current(0)
country.place(x=10, y=10)

frame.mainloop()
"""

# Task 13.6
    # Create Table (Data Table)

# Task 13.7 (Mini-Project)
    # Create CRUD Application using Tkinter

# Layouts
    # pack
    # grid
    # place

# pack()
"""
frame = Tk()
frame.title("My Window")
frame.geometry("400x250")
frame.resizable(False, False)
icon = PhotoImage(file="images/icon.png")
frame.iconphoto(False, icon)

btn1 = Button(frame, text="Button1")
btn1.pack(side=LEFT)
btn2 = Button(frame, text="Button2")
btn2.pack(side=RIGHT)
btn3 = Button(frame, text="Button3")
btn3.pack(side=TOP)
btn4 = Button(frame, text="Button4")
btn4.pack(side=BOTTOM)

frame.mainloop()
"""

# Grid
"""
frame = Tk()
frame.title("My Window")
frame.geometry("400x250")
frame.resizable(False, False)
icon = PhotoImage(file="images/icon.png")
frame.iconphoto(False, icon)

lbl_name = Label(frame, text="NAME : ").grid(row=0, column=0)
txt_name = Entry(frame).grid(row=0, column=1)

frame.mainloop()
"""

# place
"""
lbl_id = Label(frame, text="Enter ID : ")
lbl_id.place(x=10, y=10)
"""

# https://towardsdatascience.com/top-10-python-gui-frameworks-for-developers-adca32fbe6fc