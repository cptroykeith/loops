# Repeated Steps
'''
n = 8
while n > 0 :
    print(n)
    n = n - 1
print('Blastoff')
print(n)
'''
'''
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1
'''
#definite loop with strings
'''
friends = ['roy', 'william', 'keith']
for friend in friends :
    print('Happy new year:', friend)
print('Done!')
'''
#Finding the largest value
'''
from ast import Num


largest_so_far = -1
print('Before',largest_so_far)
for the_num in [9, 41, 13, 56, 23, 89, 12] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far,the_num)
print('After', largest_so_far)
'''
#counting in aloop
'''
zork = 0 
print('Before',zork)
for thing in (9, 43, 37, 4, 8 ,73, 23):
    zork = zork + 1
    print(zork, thing)
print('After',zork)
'''
#summing in a loop
'''
zork = 0 
print('Before',zork)
for thing in (9, 43, 37, 4, 8 ,73, 23):
    zork = thing + zork
    print(zork, thing)
print('After',zork)
'''
#finding the average in aloop
'''
count = 0
sum = 0 
print('Before',count, sum)
for value in (9, 43, 37, 4, 8 ,73, 23):
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After',count, sum, sum / count)
'''
#filtering in a loop
'''
for value in [9, 41, 56, 18, 12, 4]:
    if value > 20:
        print('Large number',value)
print('After')
'''
#finding the smallest value
'''
smallest = None 
print ('Before')
for value in [9, 41, 56, 18, 12, 4]:
    if smallest is None :
        smallest = value 
    elif value < smallest:
        smallest = value
    print(smallest, value)
#print ('After', smallest)
'''

#finding the largest value
''''
largest = None 
print ('Before')
for value in [9, 41, 56, 18, 12, 4]:
    if largest is None :
       largest = value 
    elif value > largest:
        largest = value
    print(largest, value)
print ('After', largest)
'''
#execise.program which prints total, count, average of numbers once the user press done.
'''
num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
         fval = float(sval)
    except:
        print('invalid input')
        continue
    #print(fval)
    num = num + 1
    tot = tot + fval 
#print('ALL DONE')
print(tot,num,tot/num)
'''
#pyramid
'''
print("Number Pattern")
row = 5
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end= ' ')
    print(" ")     
    '''
  

# print a multiplication table of given numbe
'''
num = 2 
for value in range(1, 11, 2):
    p = num * value
    print(p)
    '''
#The number must be divisible by five
#If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop

'''  
numbers = [12, 75, 150, 180, 145, 545, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
         print(item)
         '''
# Count the total number of digits in a number
'''
from itertools import count


num = 75869
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print("Total digits are:", count)
'''
#pattern
'''
n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()
    '''
    #Print list in reverse order using a loop
'''
list1 = [10, 20, 30, 40, 50]
new_list = reversed(list1)
for item in new_list:
     print(item)
     '''
#Display numbers from -10 to -1 using for loop
'''
for num in range(-10, 0, 1):
    print(num)
    '''
#Use else block to display a message “Done” after successful execution of for loop
'''
for i in range(5):
    print(i)
else:
    print('Done!')
    '''
#display all prime numbers within a range
for i in range(25, 50):
    if i > 1:
        for num in range(2, i):
            if(i % num) == 0:
                break
        else:
            print(i)
            