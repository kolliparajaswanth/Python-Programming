# Cumulative product of list of numbers

def cummulative_product(arglist):
    num = 1
    for i in arglist:
        num *= i
        print(num)

listr = []
n = int(input('Enter no.of elements: '))
for j in range(0, n):
    ele = int(input())

    listr.append(ele)
print('Cumulative product of given list:')
cummulative_product(list)

'''
Output:-
Enter no.of elements: 4
5
1
4
5
Cumulative product of given list:
5
5
20
100
'''
