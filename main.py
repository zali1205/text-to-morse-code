from morse import morse_dict

def cipher():
    print("Cipher")

def decipher():
    print("Decipher")

continueProgram = True

print("Welcome to the Text to Morse converter!")
while (continueProgram):
    user_input = input("Would you like to encode or decode morse code?\n").upper()
    if user_input == "ENCODE":
        cipher()
    elif user_input == "DECODE":
        decipher()
    elif user_input == "QUIT":
        continueProgram = False
        print("Goodbye!")
    else:
        print("Invalid input. Please try again!")

