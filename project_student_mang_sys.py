# Function Add Students

# 1. user say input lo.
# 2. input student data object ko variable main store karo.
# 3. variable ko student list main append karo
# 4. student data ko append karo


list_students = []

# !Function Add Students


def add_student(name, urdu, english_marks, math_marks):

    student = {
        "name": name,
        "urdu": urdu,
        "english": english_marks,
        "math": math_marks
    }

    list_students.append(student)
    return student


# !---- Main ---- Adding students data

num_students = int(input("How many students need to added:  "))

for stu in range(num_students):

    name = input("Enter student name: ")
    urdu = int(input("Enter urdu marks: "))
    english_marks = int(input("Enter english marks: "))
    math_marks = int(input("Enter math marks: "))

    student_data = add_student(name, urdu, english_marks, math_marks)


# !---- Main ---- Grade Function.

def cal_grade(percentage):

    if percentage >= 80:
        return "A Grade"
    elif percentage >= 70:
        return "B Grade"
    elif percentage >= 60:
        return "C Grade"
    elif percentage >= 50:
        return "D Grade"
    elif percentage >= 40:
        return "E Grade"
    elif percentage <= 39:
        return "Fail"
    else:
        return "Invalid Data"


# !---- Main ---- Showing Result.
for stu in list_students:

    print(stu)
    total_marks = stu["urdu"] + stu["english"] + stu["math"]

    print("Total Marks:", total_marks)
    percentage = (total_marks / 300) * 100
    print("Percentage:", round(percentage), "%")
    print(cal_grade(percentage))
