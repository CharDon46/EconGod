from tkinter import * 
from tkinter import ttk
from PIL import ImageTk, Image

window = Tk()

window.title("Econ God")

content = ttk.Frame(window, padding=(3,3,12,12))
bg_image = ImageTk.PhotoImage(Image.open("nature.png"))
#bg_image = PhotoImage(file = "nature.png")

# get the image size
w = bg_image.width()
h = bg_image.height()

# make the root window the size of the image
window.geometry("%dx%d" % (w, h))

background_label = Label(window, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

l1=Label(window, text="Welcome")
l1.grid(row=1,column=5, padx=175, pady=5)
l1.config(font=("Courier", 44))

l2=Label(window, text="Select an option from the\n menu below")
l2.grid(row=2,column=5)
l2.config(font=("Helvetica", 13, "bold"))

b1=Button(window, text="Home", width=14)
b1.grid(row=3, column=5)
b2=Button(window, text="Current Supplies", width=14)
b2.grid(row=4, column=5)
b3=Button(window, text="Update Inventory", width=14)
b3.grid(row=5, column=5)
b4=Button(window, text="Create Report", width=14)
b4.grid(row=6, column=5)
b5=Button(window, text="Faculty/Printer\n Lookup", width=14)
b5.grid(row=7, column=5)


window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=0)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

window.mainloop()