from raindrop_function import raindrop_function
print("Here we will test the code to see if it works!")

print("Making sure that the numbers will return the correct word.")
print(raindrop_function(3) == "Pling")
print(raindrop_function(5) == "Plang")
print(raindrop_function(7) == "Plong")
print(raindrop_function(11) == "11")

print("Testing numbers to see if they output combined raindrop sounds.")
print(raindrop_function(15) == "PlingPlang")
print(raindrop_function(21) == "PlingPlong")
print(raindrop_function(35) == "PlangPlong")
print(raindrop_function(105) == "PlingPlangPlong")

print("Testing random numbers to ensure that the code is functional and correct.")

print(raindrop_function(96) == "Pling")
print(raindrop_function(88) == "88")
print(raindrop_function(84) == "PlingPlong")
print(raindrop_function(64) == "64")
print(raindrop_function(57) == "Pling")

print("Testing inputs that should work including integers and whole numbers.")
print(raindrop_function(15) == "PlingPlang")
print(raindrop_function(15.0) == "PlingPlang")