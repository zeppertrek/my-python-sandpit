#Assert that a certain exception is raised
#Use the raises helper to assert that some code raises an exception:
# content of test_sysexit.py

import pytest

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()