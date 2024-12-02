from tkinter import *
from tkinter import filedialog
from utils.middleman import get_data
from utils.Backend.file_system_entities import dir, file
import json

MIN_WIDTH = 300
MIN_HEIGHT = 300

MAX_WIDTH = 900
MAX_HEIGHT = 500

filename = "No dir chosen"

analasys = {}


settings_dict ={
    "include inside method": False,
    "max depth": False,
    "show average method size": True,
    "biggest method": False,
    "smallest method": False,
    "mean comments method": False,
    "mean comments line": False,
    "mean docstrings": False
}

def browseFiles():
    global filename
    filename = filedialog.askdirectory(mustexist=True)

    l.config(text = filename)


def analyze():
    analasys = get_data(filename, settings_dict=settings_dict)
    with open("data_example.json", "w") as outfile: 
        json.dump(analasys, outfile)

def vizualise_method_size():
    pass


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
                        command = analyze) 

button_analyze.grid(row=2, column = 2)

root.mainloop()

