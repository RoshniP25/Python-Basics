print("===== STUDENT RESULT ANALYSER =====")

#list of student marks
scores = [33, 78, 55, 12, 90, 41, 39, 60]

passed = 0

#count marks
for s in scores:
    if s >= 40:
        passed += 1

print("Total students passed:", passed)