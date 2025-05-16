from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        Jar(-1)
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.deposit(3)  # Would exceed capacity (3 + 3 > 5)

    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(3)

    with pytest.raises(ValueError):
        jar.withdraw(-1)
