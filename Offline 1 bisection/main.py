import matplotlib.pyplot as LOL
import numpy as Era

lower_b = -1.99
upper_b = 0.9


def f(x):
    return x**3-2400*(x**2)-3*x+2


def root(lower_b=0, upper_b=1, max_error=0.5, max_i=20):

    root_old = 0
    root_new = 0
    err = 5
    iteration = 0
    tot=0

    if f(lower_b) * f(upper_b) > 0:
        print("Bisection method fails! No root!!!")
        return None

    while err > max_error and iteration < max_i:
        middle_b = (lower_b+upper_b)/2
        root_new = middle_b

        if f(lower_b)*f(middle_b) < 0:
            upper_b = middle_b
        elif f(upper_b)*f(middle_b) < 0:
            lower_b = middle_b
        else:
            return middle_b

        iteration += 1
        err = abs((root_new-root_old)/root_new)*100
        root_old = root_new
        tot+=1

    print(tot)
    return middle_b


def table(lower_b=0, upper_b=1, max_i=20):

    root_old = 0
    root_new = 0
    iteration = 0

    if f(lower_b) * f(upper_b) > 0:
        print("Bisection method fails! No root!!!")

    print("Iteration", "\troot", "\t\t\terror")

    while iteration < max_i:
        middle_b = (lower_b + upper_b) / 2
        root_new = middle_b

        if f(lower_b) * f(middle_b) < 0:
            upper_b = middle_b
        elif f(upper_b) * f(middle_b) < 0:
            lower_b = middle_b
        else:
            return middle_b

        iteration += 1
        err = abs((root_new - root_old) / root_new) * 100
        root_old = root_new

        print(iteration,"\t\t\t%0.7f"%middle_b,"\t\t%0.7f"%err)


print("the approximate root is: ",root(0, 1, 0.5, 20))
table(0, 1, 20)

x = Era.linspace(lower_b, upper_b, 1000000)
y = f(x)
LOL.plot(x, y)
LOL.title("Bisection method")
LOL.xlabel("x")
LOL.ylabel("y=f(x)")
LOL.grid()
LOL.show()







