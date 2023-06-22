import pytest
from conversion import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
    
    fahrenheit = celsius_to_fahrenheit(20)
    assert fahrenheit == 68
    
    fahrenheit = celsius_to_fahrenheit(0)
    assert fahrenheit == 32

    fahrenheit = celsius_to_fahrenheit(100)
    assert fahrenheit == 212
 
def test_celsius_to_fahrenheit_invalid():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("Invalid")

def test_celsius_to_fahrenheit_none():
    assert celsius_to_fahrenheit(None) is None
