from app import raindrop_function #This line, imports the function raindrop_function app.py so it can be tested here.
print("Here we will test the code to see if it works!")

print("Making sure that the numbers will return the correct word.")
#Lines 6-9 check to see if the values would return the correct output.
print(raindrop_function(3) == "Pling")
print(raindrop_function(5) == "Plang")
print(raindrop_function(7) == "Plong")
print(raindrop_function(13) == "13")


print("Testing numbers to see if they output combined raindrop sounds.")
#Lines 13-17 check to see if the values would return the correct output.
print(raindrop_function(2) == "2")
print(raindrop_function(9) == "Pling")
print(raindrop_function(21)) == "PlingPlong"


print("Testing inputs that should work including integers and whole numbers.")
#Lines 30-31 check to see if the values would return the correct output.
print(raindrop_function(27) == "PlingPlong")
print(raindrop_function(27.0) == "PlingPlong")


