series = int(input("Enter no. of digits you want the fibonacci series to be: "))
first= 0
second= 1

for i in range (0,series+1):
    print(first)

    next=first+second
    first=second
    second=next
    
