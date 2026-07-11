print("===== INTERNET SPEED CHECKER =====")

speed = float(input("Enter your internet speed(Mbps): "))

if speed >= 100:
    print("Category: Ultra=Fast")
elif speed >= 50:
    print("Category: Fast")
elif speed >= 20:
    print("Category: Moderate")
elif speed >= 10:
    print("Category: Slow")
else:
    print("Invalid speeed internet.")