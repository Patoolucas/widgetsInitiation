from tkinter import *

#Widget is a object with specific information or function

#Creating the main window widget
root = Tk() #root widget

def onClick():
    #label = Label(root, text="Click, Click, Click")
    comment = item.get()
    label = Label(root, text=comment).grid(row=0,column=0)
    print("lol" + comment)

def rbutton(value):
    label3 = Label(root, text=radio_var.get()).grid(row=5,column=1)

#Create a widgets and buttons to display in our root
label = Label(root, text="Hello World").grid(row=0,column=0)
label2 = Label(root, text="This is a CSCI 3340").grid(row=1,column=0)
button = Button(root, text="Click Here", command=onClick).grid(row=2,column=0)
item = Entry(root)
item.insert(0, "Type your favorite pie")

#dropdown menu
drop_var = StringVar()
drop_var.set("Choose pie")
drop_menu = OptionMenu(root, drop_var, "apple","cheese","lime").grid(row=6,column=2)


#Radio button setup
radio_var = IntVar()
#radio_var = StringVar() //Declaring a string variable
options = ["Option1", "Option2", "Option3", "Option4"]
counter = 0
for option in range(len(options)):
    Radiobutton(root, text=option, variable=radio_var, value=counter, command=lambda:rbutton(radio_var.get())).grid(row=0,column=3)
    counter += 1


#Radiobutton(root, text="Option1", variable=radio_var, value=1).grid(row=0,column=1)
#Radiobutton(root, text="Option2", variable=radio_var, value=2).grid(row=0,column=2)

#Packing widgets in the root
#label.pack()

#Using grids to call widgets to the window
#label.grid(row=0,column=0)
#label2.grid(row=1,column=0)
#button.grid(row=2,column=0)
item.grid(row=3,column=0)


#Call the main loop for displaying the root window
root.mainloop()



