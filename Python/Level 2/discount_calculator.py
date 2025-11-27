
price = float(input("Enter total price: "))

if price > 100:
    print("You get 20% off.")
    print("Final price:", price * 0.8)
else:
    print("No discount. Final price:", price)