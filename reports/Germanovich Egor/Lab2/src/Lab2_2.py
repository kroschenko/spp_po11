class Applicant:
    def __init__(self, name: str):
        self.name = name
        self.faculty = None
        self.grades = []

    def register_faculty(self, faculty):
        self.faculty = faculty
        faculty.add_applicant(self)

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_score(self) -> float:
        if not self.grades:
            return 0
        return sum(g.value for g in self.grades) / len(self.grades)

    def __str__(self):
        return f"Абитуриент: {self.name}, Факультет: {self.faculty.name if self.faculty else 'Не зарегистрирован'}"


class Faculty:
    def __init__(self, name: str):
        self.name = name
        self.applicants = []

    def add_applicant(self, applicant):
        self.applicants.append(applicant)

    def __str__(self):
        return f"Факультет: {self.name}"


class Exam:
    def __init__(self, name: str):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def __str__(self):
        return f"Экзамен: {self.name}"


class Grade:
    def __init__(self, value: float, applicant: Applicant, exam: Exam):
        self.value = value
        self.applicant = applicant
        self.exam = exam
        exam.add_grade(self)
        applicant.add_grade(self)

    def __str__(self):
        return f"Оценка: {self.value}, Абитуриент: {self.applicant.name}, Экзамен: {self.exam.name}"


class Teacher:
    def __init__(self, name: str):
        self.name = name

    def assign_grade(self, value: float, applicant: Applicant, exam: Exam):
        Grade(value, applicant, exam)

    def __str__(self):
        return f"Преподаватель: {self.name}"


class AdmissionSystem:
    def __init__(self):
        self.applicants = []
        self.faculties = []

    def add_applicant(self, applicant):
        self.applicants.append(applicant)

    def add_faculty(self, faculty):
        self.faculties.append(faculty)

    def admit_applicants(self, threshold: float):
        admitted = []
        for applicant in self.applicants:
            if applicant.average_score() >= threshold:
                admitted.append(applicant)
        return admitted

    def __str__(self):
        return f"Система зачислений: {len(self.applicants)} абитуриентов, {len(self.faculties)} факультетов"


def get_user_input():
    system = AdmissionSystem()

    faculties = []
    while True:
        faculty_name = input("Введите название факультета (или 'стоп' для завершения): ")
        if faculty_name.lower() == "стоп":
            break
        faculty = Faculty(faculty_name)
        system.add_faculty(faculty)
        faculties.append(faculty)
        print(f"Факультет '{faculty_name}' добавлен.")

    applicants = []
    while True:
        applicant_name = input("Введите имя абитуриента (или 'стоп' для завершения): ")
        if applicant_name.lower() == "стоп":
            break
        applicant = Applicant(applicant_name)
        print("Доступные факультеты:")
        for i, faculty in enumerate(faculties):
            print(f"{i + 1}. {faculty.name}")
        faculty_index = int(input("Выберите факультет (номер): ")) - 1
        applicant.register_faculty(faculties[faculty_index])
        system.add_applicant(applicant)
        applicants.append(applicant)
        print(f"Абитуриент '{applicant_name}' зарегистрирован на факультет '{faculties[faculty_index].name}'.")

    exams = []
    while True:
        exam_name = input("Введите название экзамена (или 'стоп' для завершения): ")
        if exam_name.lower() == "стоп":
            break
        exam = Exam(exam_name)
        exams.append(exam)
        print(f"Экзамен '{exam_name}' добавлен.")

    teachers = []
    while True:
        teacher_name = input("Введите имя преподавателя (или 'стоп' для завершения): ")
        if teacher_name.lower() == "стоп":
            break
        teacher = Teacher(teacher_name)
        teachers.append(teacher)
        print(f"Преподаватель '{teacher_name}' добавлен.")

    while True:
        print("Выберите абитуриента:")
        for i, applicant in enumerate(applicants):
            print(f"{i + 1}. {applicant.name}")
        applicant_index = int(input("Номер абитуриента (или '0' для завершения): ")) - 1
        if applicant_index == -1:
            break

        print("Выберите экзамен:")
        for i, exam in enumerate(exams):
            print(f"{i + 1}. {exam.name}")
        exam_index = int(input("Номер экзамена: ")) - 1

        print("Выберите преподавателя:")
        for i, teacher in enumerate(teachers):
            print(f"{i + 1}. {teacher.name}")
        teacher_index = int(input("Номер преподавателя: ")) - 1

        grade_value = float(input("Введите оценку: "))
        teachers[teacher_index].assign_grade(grade_value, applicants[applicant_index], exams[exam_index])
        print(f"Оценка {grade_value} выставлена абитуриенту {applicants[applicant_index].name} за экзамен {exams[exam_index].name}.")

    return system


if __name__ == "__main__":
    system = get_user_input()

    threshold = float(input("Введите порог среднего балла для зачисления: "))
    admitted = system.admit_applicants(threshold)

    print("\nСписок зачисленных:")
    for a in admitted:
        print(f"{a.name} (Средний балл: {a.average_score()})")
