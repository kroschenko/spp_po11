from abc import ABC, abstractmethod


class Student:
    def __init__(self, name):
        self.name = name

    def receive_notification(self, message):
        print(f"Студент {self.name} получил уведомление: {message}")

    def submit_lab(self, lab_work):
        print(f"{self.name} сдал работу: {lab_work}")

    def take_exam(self):
        print(f"{self.name} сдаёт экзамен")


class Teacher:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Студент {student.name} добавлен")
        else:
            print(f"Студент {student.name} уже есть в списке")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Студент {student.name} удалён")
        else:
            print(f"Студента {student.name} нет в списке")

    def notify_students(self, message):
        for student in self.students:
            student.receive_notification(message)

    def check_lab_work(self, student, lab_work):
        if student in self.students:
            print(f"Преподаватель проверяет работу {lab_work} у {student.name}")
            grade = input("Введите оценку (1-5): ")
            student.receive_notification(f"Ваша работа {lab_work} оценена на {grade}")
        else:
            print(f"Ошибка: {student.name} не найден в группе")

    def conduct_consultation(self, topic):
        self.notify_students(f"Консультация по теме: {topic}")

    def take_exam(self):
        self.notify_students("Экзамен начался!")
        for student in self.students:
            student.take_exam()

    def give_lecture(self, topic):
        self.notify_students(f"Лекция: {topic}")


def create_students():
    students = []
    n = int(input("Введите количество студентов: "))
    for i in range(n):
        name = input(f"Имя студента {i + 1}: ")
        students.append(Student(name))
    return students


def handle_teacher_actions(teacher, students):
    while True:
        print("\n--- Меню ---")
        print("1. Проверить лабораторную работу")
        print("2. Провести консультацию")
        print("3. Принять экзамен")
        print("4. Провести лекцию")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            handle_lab_check(teacher, students)
        elif choice == "2":
            topic = input("Введите тему консультации: ")
            teacher.conduct_consultation(topic)
        elif choice == "3":
            teacher.take_exam()
        elif choice == "4":
            topic = input("Введите тему лекции: ")
            teacher.give_lecture(topic)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: выберите 1-5.")


def handle_lab_check(teacher, students):
    print("\nСписок студентов:")
    for idx, student in enumerate(students, 1):
        print(f"{idx}. {student.name}")
    stud_idx = int(input("Выберите студента (номер): ")) - 1
    lab = input("Введите название работы: ")
    teacher.check_lab_work(students[stud_idx], lab)


def main():
    teacher = Teacher()
    students = create_students()

    for student in students:
        teacher.add_student(student)

    handle_teacher_actions(teacher, students)


if __name__ == "__main__":
    main()
