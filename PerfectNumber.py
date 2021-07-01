"""perfect number is a positive integer
that is equal to the sum of its proper divisors,
without itself"""
num=int(input("Enter any number:"))
x=list()
for i in range(1,num):
    if num%i==0:
        x.append(i)
sum=0
for j in x:
    sum=sum+j
if sum==num:
    print("It is a perfect number")
else:
    print("It is not a perfect number")
        
