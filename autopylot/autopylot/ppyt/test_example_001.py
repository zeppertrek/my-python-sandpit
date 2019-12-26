# content of test_example_001.py
def concato(x,y,z):
    if z == 1:
        return x + y
    else:
	    return y + x 

# 
def test_logic():
    assert concato("a", "b", 1) == "ab"
    assert concato("a", "b", 2) == "ba"
    assert concato("abrcaddasdd", "wdasdadasda", 2) == "b3332323a"