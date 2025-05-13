from numb3rs import validate


def test_format():
    assert validate(r"0.0.0.0") == True
    assert validate(r"0.0.0") == False
    assert validate(r"0.0") == False


def test_false():
    assert validate(r"0.0.0") == False
    assert validate(r"275.10.0.0") == False
    assert validate(r"5.0.200.256") == False
    assert validate(r"hi my name is ben") == False
