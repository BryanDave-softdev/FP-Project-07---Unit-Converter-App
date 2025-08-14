# FP PROJECT 07: Unit Converter App

print("=== UNIT CONVERTER APP ===")
print("1. Celsius to Fahrenheit")
print("2. Kilometers to Miles")
print("3. Kilograms to Pounds")

choice = input("Choose an option (1/2/3): ")

if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"\nResult: {celsius}°C = {fahrenheit:.2f}°F")

elif choice == "2":
    kilometers = float(input("Enter distance in kilometers: "))
    miles = kilometers * 0.621371
    print(f"\nResult: {kilometers} km = {miles:.2f} miles")

elif choice == "3":
    kilograms = float(input("Enter weight in kilograms: "))
    pounds = kilograms * 2.20462
    print(f"\nResult: {kilograms} kg = {pounds:.2f} pounds")

else:
    print("\nInvalid option. Please run the program again.")
