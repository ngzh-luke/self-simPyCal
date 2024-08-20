""" A running point of the app """

from tkinter import *
from tkinter import ttk
from configs.tkConfig import configs


rootWindow = Tk(**configs)
ttk.Button(rootWindow, text="Hello World").grid()
rootWindow.mainloop()
