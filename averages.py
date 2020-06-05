# Rachel Alexander
# rsa7ft

"""
mean function: calculate mean.

median function: output middle number for every order combination.

rms function: calculate rms.

middle_average function: calculate mean, median, and rms, and then return median of those three values.

"""


def mean(a, b, c):
    return (a + b + c)/3


def median(a, b, c):
    if (a <= b <= c):
        return b
    elif (c <= b <= a):
        return b
    elif (a <= c <= b):
        return c
    elif (b <= c <= a):
        return c
    elif (b <= a <= c):
        return a
    else:
        return a


def rms(a, b, c):
    x = (a**2 + b**2 + c**2)/3
    return x**(1/2)


def middle_average(a, b, c):
   avg = mean(a,b,c)
   mid = median(a,b,c)
   root_mean_sq = rms(a,b,c)
   return (median(avg, mid, root_mean_sq))

