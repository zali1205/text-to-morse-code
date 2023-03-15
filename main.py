from morse import morse_dict

def find_file():
    print("Please place your text file to be encoded into the 'input' folder.")
    while True:
        user_input = input("Please enter the full name of the file to be encoded.\n")
        try:
            with open(f"input/{user_input}", 'r') as file:
                data_lines = file.readlines()
                break
        except FileNotFoundError as e:
            print(f"{e}")
            print("File does not exist! Please try again!")
    return data_lines

def ouput_to_file(encoded_text: str):
    print("The output file will be placed in the 'output' folder.")
    while True:
        user_input = input("Please enter the name for your text file.\n")
        try:
            with open(user_input, 'w') as file:
                file.write(encoded_text)
                break
        except FileNotFoundError as e:
            print(f"{e}")
            print("File does not exist! Please try again!")
    print("Successfully created the output file!")

def encode():
    user_input = input("Would you like to encode a text file or enter text manually? F - File | Enter - Text/Continue \n").lower()
    data_lines = []
    if user_input == "f":
        data_lines = find_file()
    else:
        data = input("Please enter the text you would like to encode into Morse code.\n").lower() 
        data_lines.append(data)
   
    encoded_lines = []
    encoded_text = ""

    for line in data_lines:
        for char in line.lower().strip():
            if char == ' ':
                encoded_text = encoded_text[:-1]
                encoded_text += "/"
            else:
                encoded_text += morse_dict.get(char, '#') + " "
        encoded_lines.append(encoded_text)
        encoded_text = ""

    user_input = ("Encoding complete! Would you like to print to console or to an output file? F - File | Enter - Console").lower()
    if user_input == "f":
        output_to_file(encoded_lines)
    else:
        for line in encoded_lines:
            print(line)

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

