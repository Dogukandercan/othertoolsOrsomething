import os
import time

word1 = "dogukan"
word2 = "dercan"
word3 = "gitar"


punctuation1 = "*"
punctuation2 = "."

a = word1[0]
b = word1[0:2]
c = word1[0:3]

x = word2[0]
y = word2[0:2]
z = word2[0:3]




w = 1
while w < 1000:
	print(word1 + str(w))
	w += 1

w = 1
while w < 1000:
    print(word1 + str(w) + punctuation1)
    w += 1

w = 1
while w < 1000:
    print(str(w) + word1 + punctuation1)
    w += 1

w = 1
while w < 1000:
    print(str(w) + word1 + punctuation2)
    w += 1

w = 1
while w < 1000:
    print(punctuation1 + str(w) + word1 + punctuation2)
    w += 1

w = 1
while w < 1000:
    print(punctuation1 + word1 + str(w)  + punctuation2)
    w += 1
# tekliler
w = 100000
while w < 10000000:
    print(a + str(w) + punctuation1)
    w += 1
w = 100000
while w < 10000000:
    print(a + str(w) + punctuation2)
    w += 1

w = 10000
while w < 1000000:
    print(b + str(w) + punctuation1)
    w += 1
w = 10000
while w < 1000000:
    print(b + str(w) + punctuation2)
    w += 1

w = 1000
while w < 100000:
    print(c + str(w) + punctuation1)
    w += 1
w = 1000
while w < 100000:
    print(c + str(w) + punctuation2)
    w += 1
"""
w = 8
while w < 100000:
    print(x + a + str(w) + punctuation1)
    w += 1

# x with b
w = 8
while w < 100000:
    print(x + b + str(w) + punctuation1)
    w += 1

# x with c
w = 8
while w < 100000:
    print(x + c + str(w) + punctuation1)
    w += 1

# y with a
w = 8
while w < 100000:
    print(y + a + str(w) + punctuation1)
    w += 1

# y with b
w = 8
while w < 100000:
    print(y + b + str(w) + punctuation1)
    w += 1

# y with c
w = 8
while w < 100000:
    print(y + c + str(w) + punctuation1)
    w += 1

# z with a
w = 8
while w < 100000:
    print(z + a + str(w) + punctuation1)
    w += 1

# z with b
w = 8
while w < 100000:
    print(z + b + str(w) + punctuation1)
    w += 1

# z with c
w = 8
while w < 100000:
    print(z + c + str(w) + punctuation1)
    w += 1

"""








