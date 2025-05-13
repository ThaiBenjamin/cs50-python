from plates import is_valid

def test_two_letters():
    assert is_valid("111111") == False

def test_max_six_letters():
    assert is_valid("AAAAAAAAAA") == False

def test_num_mid():
    assert is_valid("BA2AAB") == False

def test_check_zero():
    assert is_valid("BAA002") == False

def test_alphanumeric():
    assert is_valid("AA.AAA") == False
    assert is_valid("AA?AAA") == False
    assert is_valid("AAA AA") == False
    
