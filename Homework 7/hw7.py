# Emily Black
# 04/24/17
# Assignment 7 - Python Project
# Python Version 3.5

# Generates all positive powers of three
def threes():
    a = 1
    while(True):
        yield 3 ** a
        a += 1

# Author: Dr. Cheng
def is_prime(b):
    if b < 2:
        return False
    elif b == 2:
        return True
    else:
        i = 2
        while i*i <= b:
            if b%i == 0:
                return False
            i += 1
        return True

# Author: Dr. Cheng
def primes():
    yield 2
    j = 3
    while(True):
        if is_prime(j):
            yield j
        j += 2

# Generates all interesting numbers (power of three + prime)
def interesting(c):
    while(True):
        output = is_interesting(c)
        if output != False:
            yield output
        c += 1

# Tests if a number is interesting
def is_interesting(d):
    for k in threes():
        if k >= d:
            return False
        elif is_prime(d-k):
            return k+(d-k)

# Finds 20 consecutive interesting numbers after e*10
def student_id(e):
    counter = 0
    for l in interesting(e*10):
        if counter > 19:
            break
        else:
            yield l
            counter += 1

# Tests interesting method
nk = interesting(1)
for jk in nk:
    if jk > 28:
        break
    else:
        print(jk)

# Tests student_id method
nk = student_id(112945795)
for jk in nk:
    print(jk)
