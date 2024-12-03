# 18.11.2024
# simple morse code translator (both directions)
# -- .- .-. .-.. --- -.

# table stolen from stack exchange
encode_table = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    " ": "SPACE",
}
import time
# make decode table by turning encode table around
keys = list(encode_table.values())
values = list(encode_table.keys())
decode_table = {}
for i in range(0,len(keys)):
    decode_table.update({keys[i]:values[i]})

# main logic (had to look it up)
def encode(text=""):
    encoded = " ".join(encode_table[x] for x in text)
    return encoded.replace("SPACE"," ")
def decode(code=""):
    decoded = code.replace("   "," SPACE ").split(" ")
    return "".join(decode_table[x] for x in decoded)

# main program
while True:
    choice = input("\nDo you want to encode or decode? (e/d): ")
    if choice == "e":
        userinput = str(input("\nType the word you want to encode.\n")).upper()
        try:
            print(f"\nTranslation: {encode(userinput)}")
            choice2 = input("\nWant to keep going? (y/n)")
            if choice2 != "y":
                print("\nOkay, bye (° - °)ﾉ\n")
                time.sleep(5)
                break   
        except:
            print("\nOnly use letters, numbers, space, '.', '?' and ','\n")
    elif choice == "d":
        userinput = str(input("\nType the code using - and . \nSeperate letters with space and words with 3 spaces:\n"))
        try:
            print(f"Translation: {decode(userinput)}")
            choice2 = input("\nWant to keep going? (y/n)")
            if choice2 != "y":
                break   
        except Exception as e:
            print(f"\nYour input could not be converted. Please check for typos!\n")
            print(e)
    else:
        print("\nInvalid choice! Try again.\n")
  
        
    

