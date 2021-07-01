#Armstrong number is a number that is equal to the sum of cubes of its digits
num=int(input("Enter any number:"))
num=str(num)
sum=0
for i in num:
    sum=sum+((int(i))**3)
num=int(num)
if num==sum:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")

