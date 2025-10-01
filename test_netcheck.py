from netcheck import is_port_open

def test_port_open_google():
    assert is_port_open("google.com", 443) == True

def test_port_closed_google():
    assert is_port_open("google.com", 23) == False