from tkinter import * 
from tkinter import ttk
from PIL import ImageTk, Image

window = Tk()

window.title("Organum")

#Inventory Search Input Box
search_inventory=StringVar()
e1=Entry(window,textvariable=search_inventory)
e1.grid(row=1,column=3)

#Faculty Search Input Box
search_faculty=StringVar()
e2=Entry(window,textvariable=search_faculty)
e2.grid(row=11,column=3)

#Inventory Buttons for Search and Update
b1=Button(window, text="Search", width=12)
b1.grid(row=1, column=4)
b2=Button(window, text="Update", width=12)
b2.grid(row=1, column=1)

#Faculty Buttons for Search and Update
b3=Button(window, text="Search", width=12)
b3.grid(row=11, column=4)
b4=Button(window, text="Update", width=12)
b4.grid(row=11, column=1)

#Inventory View 
list1=Listbox(window, height=10, width=100)
list1.grid(row=2, column=1, rowspan = 6, columnspan= 6)

#Faculty View
list2=Listbox(window, height=11, width=100)
list2.grid(row=12, column=1, rowspan = 6, columnspan= 6)

#Inventory Scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=6, rowspan=6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

#Faculty Scrollbar
sb2 = Scrollbar(window)
sb2.grid(row=12, column=6, rowspan=6)

list2.configure(yscrollcommand = sb2.set)
sb2.configure(command = list2.yview)

#Nothing past this 
window.mainloop()