#find sum of even numbers upto n

a = int(input("type your number "))
sum=0
for i in range(0 ,a+1):
    if(i % 2==0):
        sum+=i
print(sum)
