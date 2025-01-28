from src.app import add_numbers

def test_add_numbers():
    assert add_numbers(5, 3) == 8
    assert add_numbers(-1, 1) == 0

