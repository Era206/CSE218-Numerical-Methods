import numpy as np

def f(t):
    return 2000*(np.log(140000/(140000-(2100*t)))) - 9.8*t

def total_trapezoid(lower_bound, upper_bound, n):
    per_division = (upper_bound-lower_bound)/n;
    low = lower_bound;
    up = lower_bound +  per_division;
    sum = 0
    while n>0 :
        sum += ((up-low) * (f(up)+f(low))) / 2;
        up += per_division;
        low += per_division;
        n-=1;

    return sum;

def table_trapezoid(lower_bound, upper_bound, n):
    serial = 1
    old_sum = 0
    new_sum = total_trapezoid(lower_bound, upper_bound, serial)
    error = 0
    print("Divisions", "\tCalculated sum", "\t\t\tRelative Error")
    while serial <= n :
        if serial == 1:
            error = 0
        else:
            error = abs((new_sum-old_sum)/new_sum)*100

        print(serial, "\t\t\t%0.7f" % new_sum, "\t\t\t%0.7f" % error)

        serial += 1
        old_sum = new_sum
        new_sum = total_trapezoid(lower_bound, upper_bound, serial)


n= int(input("Enter number of divisions for trapezoid:"))
print(total_trapezoid(8, 30,n))
table_trapezoid(8, 30, 5)

def total_simpson(lower_bound, upper_bound, n):
    per_division = (upper_bound-lower_bound)/n
    low = lower_bound
    up = lower_bound +  per_division
    sum = 0
    while n>0 :
        sum += ((up-low) * (f(up)+f(low) + 4*f((up+low)/2))) / 6
        up += per_division
        low += per_division
        n -= 1

    return sum

def table_simpson(lower_bound, upper_bound, n):
    serial = 1
    old_sum = 0
    new_sum = total_simpson(lower_bound, upper_bound, (serial))
    error = 0
    print("Divisions", "\tCalculated sum", "\t\t\tRelative Error")
    while serial <= (n) :
        if serial == 1:
            error = 0
        else:
            error = abs((new_sum-old_sum)/new_sum)*100

        print((serial*2), "\t\t\t%0.7f" % new_sum, "\t\t\t%0.7f" % error)

        serial += 1
        old_sum = new_sum
        new_sum = total_simpson(lower_bound, upper_bound, (serial))

n= int(input("Enter number of divisions for Simpson:"))
print(total_simpson(8, 30, n))
table_simpson(8, 30, 5)