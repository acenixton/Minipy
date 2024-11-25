# 16.11.2024
# Trying to make a tic-tac-toe game with the things I learned so far.
# Two players enter a position in turns and the program shows the new board after every input.
# Program automatically switches between x and o.

import time
import tkinter as tk

# testing if someone got 3 in a row    
def wincon(field):
    # there is probably a more elegant way to do this, will look it up later
    row1 = field[1] == field[2] and field[1] == field[3]
    row2 = field[4] == field[5] and field[4] == field[6]
    row3 = field[7] == field[8] and field[7] == field[9]
    col1 = field[1] == field[4] and field[1] == field[7]
    col2 = field[2] == field[5] and field[2] == field[8]
    col3 = field[3] == field[6] and field[3] == field[9]
    dia1 = field[1] == field[5] and field[1] == field[9]
    dia2 = field[3] == field[5] and field[3] == field[7]
    checklist = [row1,row2,row3,col1,col2,col3,dia1,dia2]
    
    if True in checklist:
        return True
    else:
        return False
    
# gives back current player  
def whooseturn():
    if turn % 2 == 0:
        return 2
    else:
        return 1
    
# dict for cells in game (so I don't have to fuck around with index stuff)
def init():
    field = {1:"1", 2:"2", 3:"3",4:"4", 5:"5", 6:"6",7:"7", 8:"8", 9:"9"}
    print(f"{"\n":<18}{"Tic-Tac-Toe game":^}{"\n":>20}")
    print(f"{"Players enter the number of the field they want to mark:":<5}\n")
    return field

w = 20
h = 10
root = tk.Tk()
root.geometry('800x800+500+100')
root.resizable(0,0)
# make sub-container so game board is centered

# each cell is a button, that changes it's symbol based on the turn it is clicked in
one = tk.Button(root,width=w,height=h)
one.grid(column=0,row=0,padx=10,pady=10)
two = tk.Button(root,width=w,height=h)
two.grid(column=1,row=0,padx=10,pady=10)
three = tk.Button(root,width=w,height=h)
three.grid(column=2,row=0,padx=10,pady=10)


root.mainloop()
# # gameplay-loop
# #global turn 
# turn = 0
# field = init()
# end = False
# while True:
#     turn += 1
            
#     ausgabe(field)
#     cell = int(input(f"Player {whooseturn()}: "))
#     if whooseturn() == 1:
#         field[cell] = "x"
#     else:
#         field[cell] = "o"
    
#     if wincon(field):
#         print(f"{"\nCongratulations, Player":<18} {whooseturn()}, you won!\n")
#         ausgabe(field)
#         print(f"{"\nWanna play again?":<18}")
#         end = True
#     elif turn == 9:
#         print(f"\nNoone wins. Try again?")
#         end = True
        
#     if end:    
#         nexttry = input("Type 'y' if you want to try again: ")
#         if nexttry == "y":
#             turn = 0
#             field = init()
#             end = False
#         else:
#             print("\nOkay, bye (° - °)ﾉ\n")
#             time.sleep(5)
#             break
   
    
    
    
    
    
        
        





