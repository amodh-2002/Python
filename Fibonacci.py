"""The Fibonacci Sequence is the series of numbers:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
The next number is found by adding up the two numbers before it."""
a=0
b=1
print(a)
print(b)
for i in range(1,10+1):
    c=a+b
    print(c)
    a=b
    b=c
