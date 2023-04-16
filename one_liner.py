# concat coin sign with a list of numbers
#--One Liners --#

# Task No. 1 #
# implement the following functions:
# 1 # a function that adds a $ sign before each number in the provided list of numbers.
# 2 # a function that sums the digits of a given number
# 3 # a function that doubles each letter in a string and print the new string
# 4 # a function that returns a list of all numbers divided by 4 from 1 to a given number


# 1 #

def combine_coins(sign, number_list):
    return list(map(lambda y: sign+y, list(map(str, number_list))))


print(combine_coins('$', range(5)))


# 2 #

def sum_of_digits(number):
    return sum(map(int, str(number)))


print(sum_of_digits(999))


# 3 #

def double_l(letter):
    return ' '.join([letter, letter])


def double_letter(my_string):
    return ' '.join(list(map(double_l, my_string)))


print(double_letter('Lior Trieman rules!'))

# 4 #


def four_divider(n):
    """Return a list of all integers divisible by 4 between 1 and n"""
    return list(filter(lambda x: x % 4 == 0, range(1, n+1)))


print(four_divider(9))
print(four_divider(11))
print(four_divider(22))






#print(sum_of_digits(104))


