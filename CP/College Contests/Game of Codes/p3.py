# Akash Kandpal
# My Domain => http://harrypotter.tech/
from fractions import gcd
import math
from itertools import permutations

def readInts():
    return list(map(int, raw_input().strip().split()))
def readInt():
    return int(raw_input())
def readIntsindex0():
    return list(map(lambda x: int(x) - 1, input().split()))
def readStrs():
    return raw_input().split()
def readStr():
    return raw_input()
def numlistTostr(list1):
    return ''.join(list1)
def strlistTostr(list1):
    return ''.join(str(e) for e in list1)
def strTolist(str):
    return str.split()
def strlistTointlist(str):
    return map(int, str)
def slicenum(number,x):
    return int(str(number)[:x])
def precise(num):
    return "{0:.10f}".format(num)
def rsorted(a):
    return sorted(a,reverse=True)
def binar(x):
    return '{0:031b}'.format(x)
def permute(word):
    perms = [''.join(p) for p in permutations(word)]
    # print perms
    return set(perms)

n = readInt()
a = [4,6,8]

for i in range(4,n+1):
    c= (i/2-1)*2+i/2
    if(i%2==1):
        c+=1
    # print c
    a.append(4*i-2*c)
# print a
print a[n-1]




'''
2
'''
