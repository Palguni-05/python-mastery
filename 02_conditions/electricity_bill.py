units = int(input("Enter the number of units consumed: "))

if units < 0:
    print("Invalid number of units.")

elif units <= 100:
    bill = units * 10
    print("Electricity Bill: "+str(bill)+ "rupees")

elif units <= 200:
    bill = units * 20
    print("Electricity Bill: "+str(bill)+ "rupees")

else:
    bill = units * 50
    print("Electricity Bill: "+str(bill)+ "rupees")