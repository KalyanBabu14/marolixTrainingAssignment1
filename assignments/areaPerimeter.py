
print("Menu:")
print("1. Calculate Area")
print("2. Calculate Perimeter")
print("3. Exit")
    
choice = input("Enter your choice (1/2/3): ")
    
if choice == '1':
    print("calculate Area")
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print(f"The area is {area}")
    
elif choice == '2':
    print("calculate Perimeter")
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    perimeter = 2 * (length + width)
    print(f"The perimeter is {perimeter}")
    
elif choice == '3':   
    print("Exiting the program.")

else:
    print("Invalid choice. Please choose a valid option (1/2/3).")