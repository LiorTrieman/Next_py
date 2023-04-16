# write functions that will cause the following exceptions:

'''
'pIteration
ZeroDivisionError
AssertionError
ImportError
KeyError
SyntaxError
IndentationError
TypeError'


# def variables
num_list = [1, 2, 3, 4, 5, 6, 7]  # list on numbers
y = [1, 2, 3]
x1 = 9
x2 = 0

# def functions


def divide(x, y):
    print(x/y)


def print_next(item):
    x = iter(item)
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())


def print_list(list_of_num):
    for item in range(0, 10):
        print(list_of_num[item])

def indent_error():
    print("hi")
    #    print("by")
# print_list(num_list)

#print_next(y)
divide(x1, x2)
indent_error()


def read_file(file):
    try:
        f = open(file, 'r')
    except:
        print("no such file")
    else:
        print("This is the content from the file!")
        f.close()
    finally:
        print("end of function")


read_file("no_file.txt")

'''
# UnderAge Exception
def __init__(self, arg):
    self._arg = arg


def __str__(self):
    return "Provided argument %s is not a positive integer." % self._arg



class UnderAgeE(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        years = 18-self._arg
        return "you are under age, you will be 18 in %s years" % years


def send_invitation(name, age):
    if int(age) < 18:
        raise UnderAgeE(age)
    else:
        print("You should send an invite to " + name)


#send_invitation("lior", 17)

import re
# function that check is username and pass are correctly defined:

def check_input(username, password):
    # user name 3-16, englise, under_line,and number
    # pass 8-40, small and large english, number and a sign
    characherRegex = re.compile(r'[^a-zA-Z0-9.]')
    if len(username) < 3:
        raise UsernameTooShort(len(username))
    if len(username) > 16:
        raise UsernameTooLong(len(username))
    if len(password) < 8:
        raise PasswordTooShort(len(password))
    if len(password) > 40:
        raise PasswordTooLong(len(password))
    else:
        print("OK")



## ALL EXCEPTIONS

class UnderAgeE(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        years = 18-self._arg
        return "you are under age, you will be 18 in %s years" % years

class UsernameTooShort (Exception):
    def __init__(self,username_len):
        self.username_len = username_len
    def __strn__(selfs):
        return "username is too short"


class UsernameTooLong (Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "username is too long"


class PasswordTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "pass is too short"


class PasswordTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg
    def __str__(self):
        return "pass is too short"


#check_input("LIR", "GGGGGGG")
#check_input("1", "2")
#check_input("0123456789ABCDEFG", "2")
check_input("A_a1.", "12345678")
check_input("A_1", "2")
check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
check_input("A_1", "abcdefghijklmnop")
check_input("A_1", "ABCDEFGHIJLKMNOP")
check_input("A_1", "ABCDEFGhijklmnop")
check_input("A_1", "4BCD3F6h1jk1mn0p")
check_input("A_1", "4BCD3F6.1jk1mn0p")