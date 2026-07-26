atm_cvv = input("Enter your atm card cvv: ")
pin = input("Enter your pin: ")

if atm_cvv == "123" and pin == "321":
    print("you can withdraw your money")
else:
    print("Invalid atm cvv or pin. Try again!!")