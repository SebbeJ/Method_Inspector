from tkinter import *
from tkinter import filedialog
from utils.Backend.main

MIN_WIDTH = 300
MIN_HEIGHT = 300

MAX_WIDTH = 500
MAX_HEIGHT = 500

filename = "No dir chosen"

settings_dict ={
    "include inside method": False,
    "max depth": False,
    "show average method size": True,
    "biggest method": False,
    "smallest method": False,
    "mean comments method": False,
    "mean commetns line": False,
    "mean docstrings": False
}

def browseFiles():
    global filename
    filename = filedialog.askdirectory(mustexist=True)
    
    

    l.config(text = filename)


root = Tk()

#Setting size of window
# Adjust size
root.geometry("400x400")
 
root.minsize(MIN_WIDTH, MIN_HEIGHT)
root.maxsize(MAX_WIDTH, MAX_HEIGHT)

Label(root, text='Please enter path to dir: ').grid(row=0)
l = Label(root, text="")
l.grid(row=2)

button_explore = Button(root, 
                        text = "Browse Files",
                        command = browseFiles) 

e1 = Entry(root)
e1.grid(row=0, column=1)
button_explore.grid(row=0, column=2)

button_analyze =  Button(root, 
                        text = "Analyze",
                        command = browseFiles) 

root.mainloop()

