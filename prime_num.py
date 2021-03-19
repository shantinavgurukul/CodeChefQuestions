n = int(input())
num = 2
a=1
while a<=n:
    i = 2
    while i*i<=num: # time limitation ko kam krne ke liy use kiya hai i*i jisse first condition hi wrong ho jaye.
        if num%i==0:
            num=num+1
            break
        else:
            i=i+1
    else:
        print(num)
        a=a+1
        num=num+1