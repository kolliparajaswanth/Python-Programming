from statistics import mean, median, mode


lst = []
noOfElements = int(input("Enter no.of elements: "))
for i in range(noOfElements):
    ele = int(input("Enter element "+str(i+1)+": "))
    lst.append(ele)

print("List:",lst)
print("Mean of given list: ", mean(lst))
print("Median of given list: ", median(lst))
print("Mode of given list: ", mode(lst))
