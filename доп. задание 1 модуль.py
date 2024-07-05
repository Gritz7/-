grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
average_grades = {students: sum(grades[q]) / len(grades[q]) for q, students in enumerate(sorted_students)}
print(average_grades)
student_name = input("Введите имя ученика: ")
if student_name in average_grades:
    print(f"Средний балл ученика {student_name}: {average_grades[student_name]}")


