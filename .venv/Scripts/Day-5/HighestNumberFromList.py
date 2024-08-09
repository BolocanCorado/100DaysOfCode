#Find highest score from a list
print("Find highest score from a list")
student_score = [123, 41, 1231, 21, 23, 22, 2310]

highest_score = [0]

for score in student_score:
    if score > highest_score[0]:
        highest_score[0] = score
print(highest_score)