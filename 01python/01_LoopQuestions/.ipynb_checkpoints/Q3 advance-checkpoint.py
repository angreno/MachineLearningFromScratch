#now suppose in last question we want to skip certain iteration let say we want to skip 5th iteration

a = int(input("type you number"))
for i in range (1, 11):
#we'll add continue for that
    if ( i == 5 ):
        continue
    mul = a*i
    print(f"{a}x{i}={mul}")
