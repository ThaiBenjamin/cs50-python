from numb3rs import validate

def test_true():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("200.140.0.5") == True

def test_false():
    assert validate(")
