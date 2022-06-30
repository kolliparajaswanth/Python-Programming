

def cumulativeProduct(userList):
    print('Cumulative product of given list is:')
    pro = 1
    for ele in userList:
        pro *= ele
        print(pro)


numberOfElements = int(input('Enter numbe of elements in the list: '))
userList = []
for evEle in range(0, numberOfElements):
    inEle = int(input())
    userList.append(inEle)
cumulativeProduct(userList)
