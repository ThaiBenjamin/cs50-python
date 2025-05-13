from numb3rs import validate


def test_true():
    assert validate(r"0.0.0.0") == True
    assert validate(r"255.255.255.255") == True
    assert validate(r"200.140.0.5") == True

def test_false():
    assert validate(r"0.0.0") == False
    assert validate(r"275.10.0.0") == False
    assert validate(r"5.0.200.250") == False
    assert validate(r"hi my name is ben") == False
