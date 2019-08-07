def find_pling(n):
    if n % 3 == 0: #This if function checks if the number tested has 3 as a factor, if it has a factor of 3, then the output would 'Pling' if correct.
        return "Pling"
    else:
        return ""

def find_plang(n):
    if n % 5 == 0: #This if function checks if the number tested has 5 as a factor, if it has a factor of 5, then the output would 'Pling' if correct.
        return "Plang"
    else:
        return ""

def find_plong(n):
    if n % 7 == 0: #This if function checks if the number tested has 7 as a factor, if it has a factor of 7, then the output would 'Pling' if correct.
        return "Plong"
    else:
        return ""

def raindrop_function(n): #Creating a function was essential, this method would output the correct raindrop sound depending on the numbers factors.
    output = "" #This calls for a value to be stored in output

    output += find_pling(n) #This assigns Pling to the output.

    output += find_plang(n) #This also assigns Plang to the output.

    output += find_plong(n) #This also assigns Plong to the output.

    if output == "": #This if statement, checks to see if the output is empty, if its empty it will return the number being tested.
        output = str(n)

    return output

