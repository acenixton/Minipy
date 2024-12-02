# Write Python function that allows a user to enter multiple strings.
# Continuously prompt the user to enter a string until they type "done".
# Concatenate all the entered strings into a singleone  
# Separated by spaces between each string.


def snake(old_snek=str,new_tail=str):
    return old_snek+" "+new_tail


# main 
snek = ""
while True:
    addon = input("Enter words to add, type 'done' to stop: ")
    if addon == "done":
        break
    else:
        snek = snake(snek,addon)
        
print(snek)