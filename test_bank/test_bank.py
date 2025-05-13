from bank import value

def test_bank_nonsense():
    assert value("123") == 100

def test_bank_case_insensitive():
    assert value("Hello") == 0

def test_bank_regular():
    assert value("hello my name is Bob") == 0
