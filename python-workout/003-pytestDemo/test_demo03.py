# when u want to run only 1 file



def test_firstProgram():
    msg = "hello"
    assert msg == "Hi", "test Failed"




def test_creditCard():
    a = 4
    b = 6
    assert a+2 == 6, "adition do not match"


# for all files
# py.test -v -s


# for specific file
# py.test test_demo03.py -v -s


# for specifi method
# py.test -k creditCard -v -s


# https://www.youtube.com/watch?v=UZ1u0-9-r_w