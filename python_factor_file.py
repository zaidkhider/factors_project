def convert(number):
    number_inputted = ""

    if number % 3 == 0:
        number_inputted  += "Pling"

    if number % 5 == 0:
        number_inputted += "Plang"

    if number % 7 == 0:
        number_inputted += "Plong"

    if number_inputted == "":
        number_inputted = f'{number}'

    return number_inputted