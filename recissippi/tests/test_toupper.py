# content of test_toupper.py
def toUpper(sampleString):
    return str.upper(sampleString)
	
def test_function():
    assert toUpper ("abc") == "ABC"
    # what does assert 0 do ? 
    assert 0