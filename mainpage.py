from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()
root.configure(bg="purple")


root.geometry('400x400')
Label(root, text = 'From zero to muscle?', font =('Verdana', 15)).pack(side = TOP, pady = 10)
# Creating a photoimage object to use image


photo = PhotoImage(file=r"G:\Final year project\GUI\film.png")

# here, image option is used to
# set image on button
Button(root, text='Click Me !', image=photo).pack(side=TOP)

mainloop()