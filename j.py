from ArithmeticPackage import ArithmeticDemo

a = int(input('Enter a: '))
b = int(input('Enter b: '))
print('\nSum of two number is:', end='  ')
print(ArithmeticDemo.sumtwo(a, b))
print('\nSubstraction of two number is:', end='  ')
print(ArithmeticDemo.subtwo(a, b))
print('\nProduct of two number is:', end='  ')
print(ArithmeticDemo.multwo(a, b))
print('\nDivision of two number is:', end='  ')
print(ArithmeticDemo.divtwo(a, b))
