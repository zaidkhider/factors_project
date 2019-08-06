from raindrop_function import raindrop_function
print("Here we will test the code to see if it works!")

print("Making sure that the numbers will return the correct word")
print(raindrop_function(3) == "pling")
print(raindrop_function(5) == "plang")
print(raindrop_function(7) == "plong")
print(raindrop_function(11) == "11")

print("Testing composite numbers to see output")
print(raindrop_function(15) == "plingplang")
print(raindrop_function(21) == "plingplong")
print(raindrop_function(35) == "plangplong")
print(raindrop_function(105) == "plingplangplong")

print("Testing a series of 10 random numbers to ensure code is functional")

print(raindrop_function(96) == "pling")
print(raindrop_function(88) == "88")
print(raindrop_function(84) == "plingplong")
print(raindrop_function(64) == "64")
print(raindrop_function(57) == "pling")

print("Testing inputs that should work, integer values as strings and floats")
print(raindrop_function("70") == "plangplong")
print(raindrop_function("28") == "plong")
print(raindrop_function(15) == "plingplang")
print(raindrop_function(15.0) == "plingplang")