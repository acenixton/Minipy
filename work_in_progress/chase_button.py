# 25.11.2024
# a small GUI game, where the button moves every time it is pressed

import tkinter as tki
from random import *
    
def move(event):
    border = 50
    # getting values for ranges, so the button doesn't try to appear outside of the window
    minx = window.winfo_width() - (window.winfo_width()-border)
    maxx = window.winfo_width() - border
    miny = window.winfo_height() - (window.winfo_height()-border)
    maxy = window.winfo_height() - border
    # randomising button position and moving it there
    buCatch.place(x=randint(minx,maxx), y=randint(miny,maxy))

# initialising script in background
# not strictly necessary but explicit is always better than implicit
window = tki.Tk()
window.title("Catch the button!")
window.geometry('1200x900+200+100')
window.resizable(1,1)

# button creation
buCatch = tki.Button(window, text="press me",relief='flat', bg='lime',activebackground='orange', height=3)
# binding left mouse click on button to move function
buCatch.bind('<Button-1>',move)
# putting button in window 
buCatch.pack(padx=20,pady=20)

window.mainloop()