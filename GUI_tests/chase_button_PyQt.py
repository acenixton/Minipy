# 02.12.2024
# A small GUI game, where the button moves every time it is pressed
# This time with PyQt because tkinter is annoying


from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from random import *

# def move_butt(button):
#     button.move(randint(10,90),randint(10,90))

class Win(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Catch the Button!")
        self.setGeometry(100,100,910,910)
        self.UIComponents()
        # button should start in the middle
        self.setCentralWidget(self.button)
        self.show()
        
    def UIComponents(self):
        self.button = QPushButton("click me", self)
        self.button.clicked.connect(self.move_button)
        self.button.setFixedSize(100,50)
        self.button.setStyleSheet("QPushButton:hover {color:pink; background:pink}")

    # uses css-style syntax to change how the button looks
    def change_color(self):
        colors = ["green","blue","lime","yellow","pink","orange","red","white"]
        light = ["lime","yellow","pink","orange","red","white"]
        col = choice(colors)
        self.button.setStyleSheet(f"background-color:{col}")
        if col in light:
            self.button.setStyleSheet(f"color:black; background-color:{col}")
    
    # changes button's position and calls color change function       
    def move_button(self):
        self.button.move(randint(10,800),randint(10,800))
        self.change_color()
        
        

app = QApplication(sys.argv)
window = Win()  
sys.exit(app.exec())
