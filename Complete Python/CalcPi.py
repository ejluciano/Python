from decimal import Decimal, getcontext
import math

numberofdigits = int(input("Please eter the number fo decimal place "))
getcontext().prec = numberofdigits

def calc(n):
    t = Decimal(0)
    pi = Decimal(0)
    deno = Decimal(0)
    k = 0
    for k in range(n):
        t= (Decimal(-1)**k)*(math.factorial(Decimal(6)*k))*(13591409 + 545140134*k)
        deno = math.factorial(3*k)*(math.factorial(k)**Decimal(3))*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)
        pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
        pi = 1/pi
        return str(pi)
    print(calc(1))