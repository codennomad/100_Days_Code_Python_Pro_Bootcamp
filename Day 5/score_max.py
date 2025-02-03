score_student = [150, 158, 160, 85, 45, 158, 200, 180, 190, 186]

max_score = 0

for score in score_student:
    if score > max_score:
        max_score = score
    
print(max_score)