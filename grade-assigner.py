score = float(input("Enter score: "))

if score >= 90:
    grade = "A"
if score >= 80 and score < 90:
     grade = "B"
if score >= 70 and score < 80:
     grade = "C"
if score >= 60 and score< 70:
     grade = "D"
if score < 60:
     grade = "F"

print(grade)