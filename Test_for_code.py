from app import raindrop_function #This line, imports the function raindrop_function app.py so it can be tested here.


def test_fator_3():
    assert raindrop_function(3) == "Pling"
    assert raindrop_function(9) == "Pling"

def test_factor_5():
    assert raindrop_function(5) == "Plang"
    assert raindrop_function(10) == "Plang"

def test_factor_7():
    assert raindrop_function(7) == "Plong"
    assert raindrop_function(14) == "Plong"

def test_factor_3_and_5():
    assert raindrop_function(30) == "PlingPlang"

def test_factor_3_and_5_and_7():
        assert raindrop_function(105) == "PlingPlangPlong"

def test_factor_3_and_7():
    assert raindrop_function(21) == "PlingPlong"

def test_factor_5_and_7():
    assert raindrop_function(35) == "PlangPlong"


def test_factor_no_factor():
    assert raindrop_function(13) == "13"

