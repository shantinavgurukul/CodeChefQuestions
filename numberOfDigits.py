'''You're given an integer N. Write a program to calculate the sum of all the digits of N.'''
N = int(input("Enter the number="))
for i in range(N):
    digit = input("enter the number=")
    sum1=0
    for d in (digit):   
        sum1=sum1 + int(d)        
    print( sum1)
