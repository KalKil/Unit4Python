grade=input("please enter your overall grade")

grade = int(grade)


if grade <= 59:
    print("F")
elif grade >= 60 and grade <= 69:
    print("D")
elif grade >= 70 and grade <= 79:
    print("C")
elif grade >= 80 and grade <= 89:
    print("B")
elif grade >= 90 and grade <= 100:
    print("A")
