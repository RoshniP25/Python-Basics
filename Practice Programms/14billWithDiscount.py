print("===== TOTAL BILL CALCULATOR ======")

#TAKING inputs
productName = input("Enter the product name: ")
price = float(input("Enter the price of the product: ₹"))
quantity = int(input("Enter the quantity of the product: "))

#calculating total price
total = price * quantity

#applying discount(10% discount id total > 10000)
discount = 0.10 * total
finalAmount = total - discount

print(f"\nProduct: {productName}")
print(f"Total price (before discount) : ₹{total}")
print("Discount applied (10%): ₹", discount)
print("Final Bill Amount: ₹", finalAmount)
