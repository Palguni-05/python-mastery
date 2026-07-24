# String Methods in Python

name = input("Enter your full name: ")

print("Original Name :", name)
print("Uppercase     :", name.upper())
print("Lowercase     :", name.lower())
print("Title Case    :", name.title())
print("Length        :", len(name))
print("Count of 'a'  :", name.lower().count("a"))
print("Starts with A :", name.startswith("A"))
print("Ends with n   :", name.endswith("n"))
print("Replace Space :", name.replace(" ", "-"))