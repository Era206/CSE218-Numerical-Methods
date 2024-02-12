import numpy as ERA

def elimination(a, b, d):

    l = len(b)

    for col in range(0,l-1):
        for row in range(col+1, l):
            multiple = a[row, col]/a[col, col]
            a[row] = a[row] - multiple * a[col]
            b[row] = b[row] - multiple * b[col]
        if d==True:
            print(ERA.around(a, 4))
            print(ERA.around(b, 4))


    r = ERA.ones((l, 1), dtype=ERA.float32)
    for i in range(l - 1, -1, -1):
        r[i] = (b[i]-ERA.dot(a[i], r) + a[i, i])/a[i, i]

    print("Solution matrix:")
    print(ERA.around(r, 4))

n=int(input("Enter number of unknown variable:"))
print("Enter matrix:")
coeficient=ERA.zeros((n,n),dtype=ERA.float32)
constant=ERA.zeros((n,1),dtype=ERA.float32)
for i in range(n):
    for j in range(n):
        coeficient[i,j] = float(input())
for i in range(n):
    constant[i]=float(input())
print()
d = True
elimination(coeficient, constant, d)




