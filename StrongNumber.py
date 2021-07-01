num=int(input("Enter any number:"))
num=str(num)
sum=0
for i in num:
     prod=1
     for j in range(1,int(i)+1):
         prod=prod*j
     sum=sum+prod
print(sum)
    
        
