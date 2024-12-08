class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade_student(self):
        middle_grade = sum([sum(grade) for grade in self.grades.values()]) / sum(
            [len(grade) for grade in self.grades.values()])
        return middle_grade

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        result = f'Имя: {self.name}\n' \
                 f'Фамилия: {self.surname}\n' \
                 f'Средняя оценка за домашние задания: {self.average_grade_student()}\n' \
                 f'Курсы в процессе изучения: {courses_in_progress_string}\n' \
                 f'Завершенные курсы: {finished_courses_string}'
        return result

    def __eq__(self, other):
        return self.average_grade_student() == other.average_grade_student()

    def __ge__(self, other):
        return self.average_grade_student() == other.average_grade_student()

    def __lt__(self, other):
        return self.average_grade_student() == other.average_grade_student()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade_lecturer(self):
        middle_grade = sum([sum(grade) for grade in self.grades.values()]) / sum(
            [len(grade) for grade in self.grades.values()])
        return middle_grade

    def __str__(self):
        result = f'Имя: {self.name}\n' \
                 f'Фамилия: {self.surname}\n' \
                 f'Средняя оценка за лекции: {self.average_grade_lecturer()}'
        return result

    def __eq__(self, other):
        return self.average_grade_lecturer() == other.average_grade_lecturer()

    def __gt__(self, other):
         return self.average_grade_lecturer() > other.average_grade_lecturer()

    def __lt__(self, other):
         return self.average_grade_lecturer() < other.average_grade_lecturer()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}'


student_1 = Student('Ivan', 'Ivanov', 'man')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Boris', 'Borisov', 'man')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Fedor', 'Fedorov')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Petr', 'Petrov')
lecturer_2.courses_attached += ['Java']

reviewer_1 = Reviewer('Robot', 'Bender')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('Filip', 'Fry')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']

student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 10)

student_2.rate_hw(lecturer_2, 'Java', 10)
student_2.rate_hw(lecturer_2, 'Java', 8)
student_2.rate_hw(lecturer_2, 'Java', 9)

reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)

reviewer_2.rate_hw(student_2, 'Java', 8)
reviewer_2.rate_hw(student_2, 'Java', 7)
reviewer_2.rate_hw(student_2, 'Java', 9)

print(f'Проверяющие:\n\n{reviewer_1}\n\n{reviewer_2}')
print()
print()
print(f'Лекторы:\n\n{lecturer_1}\n\n{lecturer_2}')
print()
print()
print(f'Студенты:\n\n{student_1}\n\n{student_2}')
print()
print()
print(f'Результат сравнения лекторов (по средней оценке за лекции): ')
if lecturer_1.average_grade_lecturer() == lecturer_2.average_grade_lecturer():
    print(f'{lecturer_1.name} {lecturer_1.surname} == {lecturer_2.name} {lecturer_2.surname}')
else:
    print(f'{lecturer_1.name} {lecturer_1.surname} != {lecturer_2.name} {lecturer_2.surname}')
if lecturer_1.average_grade_lecturer() > lecturer_2.average_grade_lecturer() :
    print(f'{lecturer_1.name} {lecturer_1.surname} > {lecturer_2.name} {lecturer_2.surname}')
else:
    print(f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname}')
print()
print()
print(f'Результат сравнения студентов (по средней оценке за ДЗ): ')
if student_1 == student_2:
    print(f'{student_1.name} {student_1.surname} == {student_2.name} {student_2.surname}')
else:
    print(f'{student_1.name} {student_1.surname} != {student_2.name} {student_2.surname}')
if student_1 > student_2:
    print(f'{student_1.name} {student_1.surname} > {student_2.name} {student_2.surname}')
else:
    print(f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname}')

student_list = [student_1, student_2]

def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_grade_student()
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all
print()
print()
print(f"Средняя оценка всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")

lecturer_list = [lecturer_1, lecturer_2]

def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_grade_lecturer()
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all
print()
print(f"Средняя оценка всех лекторов по курсу {'Java'}: {lecturer_rating(lecturer_list, 'Java')}")


