from abc import ABC, abstractmethod
from typing import List


class Person(ABC):
    def __init__(self, name: str, person_id: int):
        self.name = name
        self.person_id = person_id

    @abstractmethod
    def display_info(self):
        pass

class Student(Person):
    def __init__(self, name: str, student_id: int):
        super().__init__(name, student_id)
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        course.add_student(self)

    def display_info(self):
        print(f"Студент: {self.name}, ID: {self.person_id}")

class Teacher(Person):
    def __init__(self, name: str, teacher_id: int):
        super().__init__(name, teacher_id)
        self.courses = []

    def create_course(self, course_name: str):
        course = Course(course_name, self)
        self.courses.append(course)
        return course

    def assign_grade(self, student, course, grade_value: int):
        grade = Grade(student, course, grade_value)
        Archive.add_grade(grade)

    def display_info(self):
        print(f"Преподаватель: {self.name}, ID: {self.person_id}")

class Course:
    def __init__(self, name: str, teacher: Teacher):
        self.name = name
        self.teacher = teacher
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def display_info(self):
        print(f"Курс: {self.name}, Преподаватель: {self.teacher.name}")
        print("Записанные студенты:")
        for student in self.students:
            print(f" - {student.name}")

class Grade:
    def __init__(self, student: Student, course: Course, grade_value: int):
        self.student = student
        self.course = course
        self.grade_value = grade_value

    def display_info(self):
        print(f"Оценка: {self.grade_value}, Студент: {self.student.name}, Курс: {self.course.name}")

class Archive:
    _grades = []

    @classmethod
    def add_grade(cls, grade: Grade):
        cls._grades.append(grade)

    @classmethod
    def display_grades(cls):
        print("Архив оценок:")
        for grade in cls._grades:
            grade.display_info()

def create_teacher():
    name = input("Введите имя преподавателя: ")
    teacher_id = int(input("Введите ID преподавателя: "))
    return Teacher(name, teacher_id)

def create_student():
    name = input("Введите имя студента: ")
    student_id = int(input("Введите ID студента: "))
    return Student(name, student_id)

def create_course(teacher):
    course_name = input("Введите название курса: ")
    return teacher.create_course(course_name)

def enroll_student(students, courses):
    if not students:
        print("Нет доступных студентов.")
        return
    if not courses:
        print("Нет доступных курсов.")
        return

    print("Выберите студента:")
    for i, student in enumerate(students):
        print(f"{i + 1}. {student.name} (ID: {student.person_id})")
    student_index = int(input("Введите номер студента: ")) - 1

    print("Выберите курс:")
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course.name} (Преподаватель: {course.teacher.name})")
    course_index = int(input("Введите номер курса: ")) - 1

    students[student_index].enroll(courses[course_index])
    print(f"Студент {students[student_index].name} записан на курс {courses[course_index].name}.")

def assign_grade(students, courses):
    if not students:
        print("Нет доступных студентов.")
        return
    if not courses:
        print("Нет доступных курсов.")
        return

    print("Выберите студента:")
    for i, student in enumerate(students):
        print(f"{i + 1}. {student.name} (ID: {student.person_id})")
    student_index = int(input("Введите номер студента: ")) - 1

    print("Выберите курс:")
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course.name} (Преподаватель: {course.teacher.name})")
    course_index = int(input("Введите номер курса: ")) - 1

    grade_value = int(input("Введите оценку: "))
    courses[course_index].teacher.assign_grade(students[student_index], courses[course_index], grade_value)
    print(f"Оценка {grade_value} выставлена студенту {students[student_index].name} за курс {courses[course_index].name}.")

def main():
    students = []
    courses = []
    teacher = None

    while True:
        print("\n--- Меню ---")
        print("1. Создать преподавателя")
        print("2. Создать студента")
        print("3. Создать курс")
        print("4. Записать студента на курс")
        print("5. Выставить оценку студенту")
        print("6. Показать курсы")
        print("7. Показать архив оценок")
        print("8. Выйти")
        choice = input("Введите ваш выбор: ")

        if choice == "1":
            teacher = create_teacher()
            print(f"Преподаватель {teacher.name} создан.")
        elif choice == "2":
            student = create_student()
            students.append(student)
            print(f"Студент {student.name} создан.")
        elif choice == "3":
            if teacher:
                course = create_course(teacher)
                courses.append(course)
                print(f"Курс {course.name} создан.")
            else:
                print("Сначала создайте преподавателя.")
        elif choice == "4":
            enroll_student(students, courses)
        elif choice == "5":
            assign_grade(students, courses)
        elif choice == "6":
            if courses:
                for course in courses:
                    course.display_info()
            else:
                print("Нет доступных курсов.")
        elif choice == "7":
            Archive.display_grades()
        elif choice == "8":
            print("Выход...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
    