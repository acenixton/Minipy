# 02.12.2024
# A small GUI game, where the button moves every time it is pressed
# This time with PyQt because tkinter is annoying

import PyQt6.QtWidgets as wi
from PyQt6.QtCore import *
import sys
from random import *

width = 900
height = 900
bump = 140
sx = width-bump
sy = height-bump

def jump():
    buJump.move(randint(bump,sx),randint(bump,sy))
    change_color()
    
def end():
    sys.exit()
# uses css-style syntax to change how the button looks
def change_color():
    colors = ["green","blue","lime","yellow","pink","orange","red","white"]
    light = ["lime","yellow","pink","orange","red","white"]
    col = choice(colors)
    buJump.setStyleSheet(f"background:{col}")
    if col in light:
        buJump.setStyleSheet(f"color:black; background:{col}")
        
app = wi.QApplication(sys.argv)
win = wi.QWidget()
win.setGeometry(100,100,width,height)
win.setWindowTitle("Chase the Button!")

buJump = wi.QPushButton("jump",win)
buJump.setFixedSize(100,50)
buJump.clicked.connect(jump)
jump()

win.setContentsMargins(50,20,50,20)
win.show()
sys.exit(app.exec())

