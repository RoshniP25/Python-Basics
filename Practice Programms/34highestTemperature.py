print("====== WEEKLY TEMPERATURE CHECK =====")

#daily temperature readings
temperature = [30.5, 32.1, 31.7, 33.0, 29.8, 34.2, 32.9]

highest = temperature[0] #assume first is max

#find maximum temp
for t in temperature:
    if t > highest :
        highest = t

print("Highest temperature:", highest)