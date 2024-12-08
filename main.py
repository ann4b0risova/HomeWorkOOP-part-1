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

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        average_grade = sum([sum(grade) for grade in self.grades.values()]) / sum([len(grade) for grade in self.grades.values()])
        result = f'Имя: {self.name}\n' \
                 f'Фамилия: {self.surname}\n' \
                 f'Средняя оценка за домашние задания: {average_grade}\n' \
                 f'Курсы в процессе изучения: {courses_in_progress_string}\n' \
                 f'Завершенные курсы: {finished_courses_string}'
        return result

    def __eq__(self):
        return (student_best.average_grade() == student_best1.average_grade())

    def __ge__(self):
        return (student_best.average_grade() >= student_best1.average_grade())

    def __lt__(self):
        return (student_best.average_grade() < student_best1.average_grade())


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        average_grade_lecturer = sum([sum(grade) for grade in self.grades.values()]) / sum([len(grade) for grade in self.grades.values()])
        result = f'Имя: {self.name}\n' \
                 f'Фамилия: {self.surname}\n' \
                 f'Средняя оценка за лекции: {average_grade_lecturer}'
        return result

    def __eq__(self):
        return (cool_lecturer.average_grade_lecturer() == cool_lecturer1.average_grade_lecturer())

    def __ge__(self):
        return (cool_lecturer.average_grade_lecturer() >= cool_lecturer1.average_grade_lecturer())

    def __lt__(self):
        return (cool_lecturer.average_grade_lecturer() < cool_lecturer1.average_grade_lecturer())


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


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)