from numb3rs import validate


def test_true():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("200.140.0.5") == True

def test_false():
    assert validate("0.0.0") == False
    assert validate("275.10.0.0") == False
    assert validate("5.0.200.250") == False
    assert validate("hi my name is ben") == False
