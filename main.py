from morse import morse_dict

def encode():
    user_input = input("Please enter the text you would like to encode into Morse code.\n").lower()
    encoded_text = ""

    for char in user_input:
        if char == ' ':
            encoded_text = encoded_text[:-1]
            encoded_text += "/"
        else:
            encoded_text += morse_dict.get(char, '#') + " "

    print(encoded_text)

def decode():
    user_input = input("Please enter the Morse code you would like to decode.\n").lower()
    
    morse_words = []
    morse_letter_to_add = ""
    for count, char in enumerate(user_input):
        if char == " ":
            morse_words.append(morse_letter_to_add)
            morse_letter_to_add = ""
        elif char == "/":
            morse_words.append(morse_letter_to_add)
            morse_words.append(" ")
            morse_letter_to_add = ""
        else:
            morse_letter_to_add += char
    if morse_letter_to_add != "":
        morse_words.append(morse_letter_to_add)

    morse_to_text_dict = {v: k for k, v in morse_dict.items()}
    decoded_text = ""

    for word in morse_words:
        if word == " ":
            decoded_text += " "
        else:
            decoded_text += morse_to_text_dict.get(word, word)
        
    print(decoded_text)

continueProgram = True

print("Welcome to the Text to Morse converter!")
while (continueProgram):
    user_input = input("Would you like to encode or decode morse code?\n").upper()
    if user_input == "ENCODE":
        encode()
    elif user_input == "DECODE":
        decode()
    elif user_input == "QUIT":
        continueProgram = False
        print("Goodbye!")
    else:
        print("Invalid input. Please try again!")

