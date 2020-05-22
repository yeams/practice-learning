import doctest
import math

def isEqual(a, b):

    # if math.fabs(a-b) < 0.000001:
    if math.isclose(a,b):
        return True
    return False

def gcd(x, y):
    if x%y != 0:
        return gcd(y, x%y)
    return y

def floatToIntRatio(inputlist):
    '''
    >>> floatToIntRatio([0.0, 1.0, 3.4, 7.8, 10.0, -4.5])
    [(0, 1), (1, 1), (7656119366529843, 2251799813685248), (8782019273372467, 1125899906842624), (10, 1), (-9, 2)]
    '''
    modlist = []
    for x in inputlist:
        divisor = 1
        while isEqual(int(x*divisor)/divisor, x) is False :
            divisor*=10
        common = gcd(x*divisor, divisor)
        modlist.append((int(x*divisor/common), int(divisor/common)))

    return modlist

if __name__ == '__main__':
    print(floatToIntRatio([0.0, 1.0, 3.4, 7.8, 10.0, -4.5]))
    # doctest.testmod()