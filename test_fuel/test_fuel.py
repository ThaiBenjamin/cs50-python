import pytest
from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()
    test_zero()
    test_value()

def test_convert():
    assert convert("1/5") == 20
    assert convert("1/100") == 1
    assert convert("5/5") == 100

def test_gauge():
    assert gauge(20) == "20%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(100) == "F"

def test_zero():
    with pytest.raises(ZeroDivisionError):
        assert convert("5/0")
def test_value():
    with pytest.raises(ValueError):
        assert convert("mouse/foot")

if __name__ == "__main__":
    main()


