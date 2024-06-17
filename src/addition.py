# app.py
# This is a test commit number 2
#just to check github actions
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
