num = int(input("Enter a number: "))

original = num
temp = num
digits = 0
total = 0

while temp > 0:
    digits = digits + 1
    temp = temp // 10

temp = original

while temp > 0:
    digit = temp % 10
    total = total + (digit ** digits)
    temp = temp // 10

if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")