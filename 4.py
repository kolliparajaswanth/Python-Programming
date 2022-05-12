# Displaying grade of student obtained by 5 subjects marks

name = input('Enter student name: ')
s1 = int(input(('Enter marks in subject 1: ')))
s2 = int(input(('Enter marks in subject 2: ')))
s3 = int(input(('Enter marks in subject 3: ')))
s4 = int(input(('Enter marks in subject 4: ')))
s5 = int(input(('Enter marks in subject 5: ')))
avg = (s1+s2+s3+s4+s5)/5
print('Grade of', name, 'is:')
if avg >= 90:
    print('O')
elif avg >= 80:
    print('A+')
elif avg >= 70:
    print('A')
elif avg >= 60:
    print('B+')
elif avg >= 50:
    print('B')
elif avg >= 40:
    print('C')
else:
    print('F')

'''
Output:-
Enter student name: Rohit
Enter marks in subject 1: 98
Enter marks in subject 2: 96
Enter marks in subject 3: 94
Enter marks in subject 4: 92
Enter marks in subject 5: 95
Grade of Rohit is:
O
'''
