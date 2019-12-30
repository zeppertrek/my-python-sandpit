#conftest.py
#
# content of conftest.py
import pytest
import smtplib

# Scope 
# Possible values are : function, class, module, package or session
@pytest.fixture(scope="module")
def ret_const_values():
    def _ret_const_values():
        return {"1": "Sanjiv", "2": "Ananya" } 
    return 	_ret_const_values

@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)