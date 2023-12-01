# Python program for implementation of Bogo Sort
import random
 
# Sorts array a[0..n-1] using Bogo sort
def bogo_sort(a):
    while (is_sorted(a)== False):
        a = shuffle(a)
    return a
# To check if array is sorted or not
def is_sorted(a):
    n = len(a)
    for i in range(0, n-1):
        if (a[i] > a[i+1] ):
            return False
    return True
 
# To generate permutation of the array
def shuffle(a):
    n = len(a)
    copy = a[:]
    b = []
    for i in range (0,n):
        r = random.randint(0,len(copy)-1)
        b.append(copy.pop(r))
    return b
k = []
for i in range(0, 999):
    k.append(random.randint(0, 999))
print(k)
print(bogo_sort(k))