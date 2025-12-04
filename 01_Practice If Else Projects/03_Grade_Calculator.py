marks = 101

if marks >=101:
    print("Enter Below 100")
    exit()

if marks >=90:
    grade = "A"
elif marks >=80:
    grade = "B"
elif marks >=70:
    grade = "C"
elif marks >=60:
    grade = "D"
else:
    grade = "F"

print("Your Grade Is ",grade)