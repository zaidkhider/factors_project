def raindrop_function(n): #Creating a function was essential, this method would output the correct raindrop sound depending on the numbers factors.

    output = "" #This calls for a value to be stored in output

    if n % 3 == 0: #This if function checks if the number tested has 3 as a factor, if it has a factor of 3, then the output would 'Pling' if correct.
        output += "Pling"

    if n % 5 == 0: #This if function checks if the number tested has 5 as a factor, if it has a factor of 3, then the output would 'Plang' if correct.
        output += "Plang"

    if n % 7 == 0: #This if function checks if the number tested has 7 as a factor, if it has a factor of 3, then the output would 'Plong' if correct.
        output += "Plong"

    if output == "": #This function checks the value (n), if the value doesn't have a factor of 3, 5 or 7 then it would output the value itself as a string
        output = str(n)

    return output


