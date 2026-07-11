print("==== CAR MILEAGE CALCULATOR =====")

#inputs from user
distance = float(input("Enter the total distance traveled (in km): "))
fuelUsed = float(input("Enter fuel used (in litres): "))

#mileage calculation
mileage = distance / fuelUsed

print(f"\nYour car's mileage is {mileage} km/litre.")