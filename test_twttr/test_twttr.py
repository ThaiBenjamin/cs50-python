from twttr import shorten

def test_twttr():
    assert shorten("to eat skunks") == "t t sknks"
    assert shorten("AEIOU") == ""
    assert shorten("AeIoU") == ""
    assert shorten("") == ""
    assert shorten("123") == "123"
    assert shorten("..A") == ".."
