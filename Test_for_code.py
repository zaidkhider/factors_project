from app import raindrop_function #This line, imports the function raindrop_function app.py so it can be tested here.

def test_factor_3(): #This part of the code creates a function that tests for a factor of 3, if there is a 3 present then the test will succeed.
    assert raindrop_function(3) == "Pling" #The assert function checks if the value within brackets which in this case is 3, will check if it outputs Pling.
    assert raindrop_function(9) == "Pling"

def test_factor_5():#This part of the code creates a function that tests for a factor of 5, if there is a 5 present then the test will succeed.
    assert raindrop_function(5) == "Plang"
    assert raindrop_function(10) == "Plang"

def test_factor_7(): #This part of the code creates a function that tests for a factor of 7, if there is a 7 present then the test will succeed.
    assert raindrop_function(7) == "Plong"
    assert raindrop_function(14) == "Plong"

def test_factor_3_and_5():#This part of the code creates a function that tests for a factor of 3 and 5, if there is a 3 and 5 present then the test will succeed.
    assert raindrop_function(30) == "PlingPlang"

def test_factor_3_and_5_and_7(): #This part of the code creates a function that tests for a factor of 3, 5 and a 7, if there is a 3, 5 and 7 present then the test will succeed.
        assert raindrop_function(105) == "PlingPlangPlong"

def test_factor_3_and_7():#This part of the code creates a function that tests for a factor of 3 and 7, if there is a 3 and 7 present then the test will succeed.
    assert raindrop_function(21) == "PlingPlong"

def test_factor_5_and_7():#This part of the code creates a function that tests for a factor of 5 and 7, if there is a 5 and 7 present then the test will succeed.
    assert raindrop_function(35) == "PlangPlong"


def test_factor_no_factor():#This part of the code creates a function that tests for a value which has no factor, if there is no factor present then the test will succeed.
    assert raindrop_function(13) == "13"

