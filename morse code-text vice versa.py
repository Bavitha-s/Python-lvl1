choice = input("Do you want to encode or decode? ").lower()

match choice:
    case "encode":
        word = input("Text: ").upper()
        morse_code = ""

        for letter in word:
            match letter:
                case "A":
                    morse_code += ".-"
                case "B":
                    morse_code += "-..."
                case "C":
                    morse_code += "-.-."
                case "D":
                    morse_code += "-.."
                case "E":
                    morse_code += "."
                case "F":
                    morse_code += "..-."
                case "G":
                    morse_code += "--."
                case "H":
                    morse_code += "...."
                case "I":
                    morse_code += ".."
                case "J":
                    morse_code += ".---"
                case "K":
                    morse_code += "-.-"
                case "L":
                    morse_code += ".-.."
                case "M":
                    morse_code += "--"
                case "N":
                    morse_code += "-."
                case "O":
                    morse_code += "---"
                case "P":
                    morse_code += ".--."
                case "Q":
                    morse_code += "--.-"
                case "R":
                    morse_code += ".-."
                case "S":
                    morse_code += "..."
                case "T":
                    morse_code += "-"
                case "U":
                    morse_code += "..-"
                case "V":
                    morse_code += "...-"
                case "W":
                    morse_code += ".--"
                case "X":
                    morse_code += "-..-"
                case "Y":
                    morse_code += "-.--"
                case "Z":
                    morse_code += "--.."
                case " ":
                    morse_code += "/"
                case _:
                    print("Invalid letter")

            morse_code += " "

        print("Morse Code:", morse_code)

    case "decode":
        morse = input("Morse code: ")
        text = ""

        for code in morse.split():
            match code:
                case ".-":
                    text += "A"
                case "-...":
                    text += "B"
                case "-.-.":
                    text += "C"
                case "-..":
                    text += "D"
                case ".":
                    text += "E"
                case "..-.":
                    text += "F"
                case "--.":
                    text += "G"
                case "....":
                    text += "H"
                case "..":
                    text += "I"
                case ".---":
                    text += "J"
                case "-.-":
                    text += "K"
                case ".-..":
                    text += "L"
                case "--":
                    text += "M"
                case "-.":
                    text += "N"
                case "---":
                    text += "O"
                case ".--.":
                    text += "P"
                case "--.-":
                    text += "Q"
                case ".-.":
                    text += "R"
                case "...":
                    text += "S"
                case "-":
                    text += "T"
                case "..-":
                    text += "U"
                case "...-":
                    text += "V"
                case ".--":
                    text += "W"
                case "-..-":
                    text += "X"
                case "-.--":
                    text += "Y"
                case "--..":
                    text += "Z"
                case "/":
                    text += " "
                case _:
                    print("Invalid Morse code")

        print("Text:", text)

    case _:
        print("Please enter 'encode' or 'decode'")
