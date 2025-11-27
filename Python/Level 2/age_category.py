
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
elif age < 65:
    print("Adult")
else:
    print("Senior")