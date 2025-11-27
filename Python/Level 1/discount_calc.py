price = float(input("Enter original price: "))
discount = float(input("Enter discount percentage: "))

final_price = price - (price * discount / 100)
print(f"Final price after discount: £{final_price:.2f}")