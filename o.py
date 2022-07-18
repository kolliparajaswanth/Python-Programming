# Import GCD from math module
from math import gcd


def gcd1(a, b):
    return gcd(a, b)


def lcm1(a, b):
    return a*b//gcd(a, b)


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print("The gcd of two numbers is", gcd1(a, b))
print("The lcm of two numbers is", lcm1(a, b))

'''
Output 1: -
Enter the value of a: 5
Enter the value of b: 1
The gcd of two numbers is 1
The lcm of two numbers is 5
'''
'''
Output 2: - 
Enter the value of a: 4
Enter the value of b: 5
The gcd of two numbers is 1
The lcm of two numbers is 20
'''
