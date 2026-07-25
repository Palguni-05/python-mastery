first_name=input("enter your first name: ")
last_name=input("enter your last name: ")
birth_year=input("enter your birth year: ")
username= first_name[:3]+ last_name[-3:] + birth_year[-2:]
print("Generated username: ",username)