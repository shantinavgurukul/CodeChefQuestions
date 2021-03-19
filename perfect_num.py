'''For example, 6 and 28 are perfect numbers because 1 + 2 + 3 = 6 and, 1 + 2 + 4 + 7 + 14 = 28. 
You are given a number n. Your task is to find whether the given no. is a Perfect Number or Not.'''
n = int(input())
for i in range(n):
    p = int(input())
    n_p = 2
    sum = 1
    while n_p*n_p <=p: # n_p*n_p (i doing bcoz time limitation ko kam krne ke liye jisse pure loop na cle hume beech me hi square mil jaye)
        if p % n_p == 0:
            if n_p == p/n_p:
                sum = sum + n_p
            else:
                sum = sum + n_p + p/n_p
        n_p=n_p+1
    if sum!=p or sum==1 :
        print('NO')
    else:
        print('YES')
