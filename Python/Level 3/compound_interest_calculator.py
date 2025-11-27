
princible = 0
rate = 0
time = 0

while princible <= 0:
    princible = float(input("Enter the princible as amount: "))
    if princible <= 0:
        print("Princible cant be lower than 0")

while rate <= 0:
    rate = float(input("Enter the rate: "))
    if rate <= 0:
        print("Rate cant be lower than 0")

while time <= 0:
    time = float(input("Enter the time: "))
    if time <= 0:
        print("Time cant be lower than 0")

print(princible)
print(rate)
print(time)


total = princible * ((1 + rate / 100) ** time)
print(f"Balance after {time} year/s: £{total:.2f}")