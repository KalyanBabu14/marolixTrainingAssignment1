age = int(input("Enter your age: \n"))

if age<=12:
    print(f"Child ({age})")
elif age>=13 and age<=19:
    print(f"Teenage ({age})")   
elif age>=20 and age<=59:
    print(f"Adult ({age})")
else:
    print(f"senior citizen ({age})")         