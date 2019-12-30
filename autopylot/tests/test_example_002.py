## content of test_example_002.py


# 
# EHLO - Extended Hello
# 
def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0  # for demo purposes


# The NOOP command does nothing else than makes the receiver to send an OK reply. 
# The main purpose is to check that the server is still connected and is able to communicate with the client.
# NOOP - No operation 
def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    assert 0  # for demo purposes