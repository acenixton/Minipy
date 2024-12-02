# 02.12.2024
# A small GUI game, where the button moves every time it is pressed
# This time with PyQt because tkinter is annoying


import PyQt6.QtWidgets as wi
from PyQt6.QtCore import QSize
import sys

def jump():
    
        
app = wi.QApplication(sys.argv)
win = wi.QWidget()
win.setGeometry(100,100,900,900)

buJump = wi.QPushButton("jump")
buJump.setFixedWidth(90)
buJump.clicked.connect(jump)

layout = wi.QVBoxLayout(win)
layout.addWidget(buJump)


win.setContentsMargins(20,20,20,20)

win.show()

sys.exit(app.exec())
































# This is a mess, let's start new
# from PyQt6.QtCore import QSize
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout
# import sys
# from random import *
# # everything in it's own class to make elements easier to grab
# class Win(QMainWindow):
    
#     def __init__(self):
#         # initialises parent class

#         super().__init__() 
#         self.setWindowTitle("Catch the Button!")
#         # sets position relative top left corner, width and height of window
#         self.setGeometry(100,100,910,910)
#         # calls initialisation for button
#         self.UIComponents()
        
#     def UIComponents(self):
#         # button should start in the middle
#         self.vbox = QVBoxLayout(self)
#         layout = QVBoxLayout()
#         self.button = QPushButton("click me", self)
#         layout.addWidget(self.button)
#         #self.button.setLayout(layout)
#         self.setCentralWidget(self.button)

#         self.button.clicked.connect(self.move_button)
#         self.button.setFixedSize(100,50)
        
#     # uses css-style syntax to change how the button looks
#     def change_color(self):
#         colors = ["green","blue","lime","yellow","pink","orange","red","white"]
#         light = ["lime","yellow","pink","orange","red","white"]
#         col = choice(colors)
#         self.button.setStyleSheet(f"background-color:{col}")
#         if col in light:
#             self.button.setStyleSheet(f"color:black; background-color:{col}")
    
#     # changes button's position and calls color change function       
#     def move_button(self):
#         self.change_color()
#         self.button.move(randint(10,800),randint(10,800))
        
        
# app = QApplication(sys.argv)
# window = Win()  
# sys.exit(app.exec())
