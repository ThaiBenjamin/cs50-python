import pytest
from datetime import date, timedelta
from seasons import minutes_to_words

def test_minutes_to_words_valid():
    yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    result = minutes_to_words(yesterday).lower()
    assert "minute" in result

def test_minutes_to_words_invalid_format():
    with pytest.raises(ValueError):
        minutes_to_words("01-01-2000")  

def test_minutes_to_words_today():
    today = date.today().strftime("%Y-%m-%d")
    result = minutes_to_words(today)
    assert result.lower().startswith("zero minutes")
