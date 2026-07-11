print("=====WORD FREQUENCY CHECKER=====")

sentence = "Python is great and learning Python makes programming easier"
word = "python"
count = 0

for w in sentence.lower().split():
    if w == word:
        count += 1

print(f"'{word}', appears", count, "times")