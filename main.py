from morse import morse_dict

def find_file():
    print("Please place your text file to be encoded or decoded into the 'input' folder.")
    while True:
        user_input = input("Please enter the full name of the file to be encoded.\n")
        try:
            with open(f"input/{user_input}", 'r') as file:
                data_lines = file.readlines()
                break
        except FileNotFoundError as e:
            print(f"{e}")
            print("File does not exist! Please try again!")
        except IOError as e:
            print(f"{e}")
            print("Could not read the file! Please make sure the file to be read has a .txt extension!")
    return data_lines

def output_to_file(encoded_lines: list):
    print("The output file will be placed in the 'output' folder.")
    while True:
        user_input = input("Please enter the name for your text file.\n")
        try:
            with open(f"output/{user_input}.txt", 'w') as file:
                for line in encoded_lines: 
                    file.write(line.upper() + "\n")
                break
        except FileExistsError as e:
            print(f"{e}")
            print("File already exists! Please try again!")
    print("Successfully created the output file!")

def encode():
    user_input = input("Would you like to encode a text file or enter the text manually? F - File | Enter - Manual Input \n").lower()
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

    user_input = input("Encoding complete! Would you like to print to console or to an output file? F - File | Enter - Console\n").lower()
    if user_input == "f":
        output_to_file(encoded_lines)
    else:
        for line in encoded_lines:
            print(line)

def decode():
    user_input = input("Would you like to decode a text file or enter the text manually? F - File | Enter - Manual Input \n").lower()
    data_lines = []
    if user_input == "f":
        data_lines = find_file()
    else:
        data = input("Please enter the text you would like to encode into Morse code.\n").lower() 
        data_lines.append(data)
    
    morse_lines = []

    for line in data_lines:
        morse_words = []
        morse_letter_to_add = ""
        for char in line.strip():
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
        morse_lines.append(morse_words)

    morse_to_text_dict = {v: k for k, v in morse_dict.items()}
    decoded_lines = []

    for line in morse_lines:
        decoded_text = ""
        for word in line:
            if word == " ":
                decoded_text += " "
            else:
                decoded_text += morse_to_text_dict.get(word, word)
        decoded_lines.append(decoded_text)
        
    user_input = input("Decoding complete! Would you like to print to console or to an output file? F - File | Enter - Console\n").lower()
    if user_input == "f":
        output_to_file(decoded_lines)
    else:
        for line in decoded_lines:
            print(line.upper())

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

