print ("Hello Welcome to Raindrop")

print ("-----------------------------")


number_inputted = int(input("Please insert a value:"))

output = ""

if number_inputted % 3 == 0:
    output += "Pling"

if number_inputted % 5 == 0:
    output += "Plang"

if number_inputted % 7 == 0:
    output += "Plong"

if output == "":
    output = str(number_inputted)

print(f"The number inserted above gives {output}")

