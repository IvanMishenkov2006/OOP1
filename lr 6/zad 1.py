class Student:
    def __init__(self, name, group_number, academic_performance):
        self.name = name
        self.group_number = group_number
        self.academic_performance = academic_performance
        self.gpa_scores = sum(self.academic_performance) / len(self.academic_performance)
    def print_info(self):
        print(f'ФИ: {self.name}\n'
              f'  Номер группы: {self.group_number}\n'
              f'  Успеваемость: {self.academic_performance}\n'
              f'  Средний балл: {self.gpa_scores}\n')
def sort_by_gpa(student):
    return student.gpa_scores
students = []
for i in range(10):
    name = input('Введите фамилию и имя студента: ')
    group_number = input('Введите номер группы: ')
    academic_performance = []
    for j in range(5):
        grade = input(f'Введите оценку за предмет {j+1}: ')
        academic_performance.append(int(grade))
    students.append(Student(name, group_number, academic_performance))
students_sorted = sorted(students, key=sort_by_gpa)
for student in students_sorted:
    student.print_info()