from math import gcd

a = int(input('Enter a:'))
b = int(input('Enter b:'))
print('GCD of a and b is: ', end='  ')
print(gcd(a, b))
print('LCM of a and b is: ', end='  ')
print((a*b//gcd(a, b)))
