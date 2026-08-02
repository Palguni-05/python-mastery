num = int(input("Enter a number: "))
factors = []
total_sum=0 
for  i in range (1,num):
    if num%i==0:
        factors.append(i)

for i in factors:
    total_sum= total_sum+ i

if num==total_sum:
    print("perfect number")
else:
    print("not a perfect number")    