class Student:
    def __init__(self, name):
        self.name = name

    def receive_notification(self, message):
        print(f"[Студент {self.name}] Уведомление: {message}")

    def submit_lab(self, lab_work):
        print(f"[Студент {self.name}] Сдал работу: '{lab_work}'")

    def take_exam(self):
        print(f"[Студент {self.name}] Сдаёт экзамен...")


class Teacher:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Студент {student.name} добавлен.")
        else:
            print(f"Студент {student.name} уже есть в списке.")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Студент {student.name} удалён.")
        else:
            print(f"Студента {student.name} нет в списке.")

    def notify_students(self, message):
        for student in self.students:
            student.receive_notification(message)

    def check_lab_work(self, student, lab_work):
        if student in self.students:
            print(f"\n[Преподаватель] Проверяет работу '{lab_work}' у {student.name}...")
            grade = input("Введите оценку (1-5): ")
            student.receive_notification(f"Работа '{lab_work}' оценена на {grade}")
        else:
            print(f"Ошибка: {student.name} не найден в группе.")

    def conduct_consultation(self, topic):
        print(f"\n[Преподаватель] Начинает консультацию по теме: '{topic}'")
        self.notify_students(f"Началась консультация: '{topic}'")

    def take_exam(self):
        print("\n[Преподаватель] Экзамен начался!")
        self.notify_students("Экзамен начался! Приступайте.")
        for student in self.students:
            student.take_exam()

    def give_lecture(self, topic):
        print(f"\n[Преподаватель] Читает лекцию: '{topic}'")
        self.notify_students(f"Лекция: '{topic}'")


def main():
    teacher = Teacher()

    # Создаём студентов
    students = []
    n = int(input("Введите количество студентов: "))
    for i in range(n):
        name = input(f"Имя студента {i+1}: ")
        students.append(Student(name))
        teacher.add_student(students[-1])

    # Меню действий преподавателя
    while True:
        print("\n--- Меню ---")
        print("1. Проверить лабораторную работу")
        print("2. Провести консультацию")
        print("3. Принять экзамен")
        print("4. Провести лекцию")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            print("\nСписок студентов:")
            for idx, student in enumerate(students, 1):
                print(f"{idx}. {student.name}")
            stud_idx = int(input("Выберите студента (номер): ")) - 1
            lab = input("Введите название работы: ")
            teacher.check_lab_work(students[stud_idx], lab)

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


if __name__ == "__main__":
    main()
