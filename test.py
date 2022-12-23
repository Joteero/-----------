from test_encryptyon import *

def test():
    a = ' som '
    x = encryption(a)
    y = decryption(x)
    print(y)
    print(a)
    assert y == a

test()