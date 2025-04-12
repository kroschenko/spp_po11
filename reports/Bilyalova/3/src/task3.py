from typing import List

class Employee:
    def __init__(self, name: str, department: str, position: str, salary: float):
        self.name = name
        self.department = department
        self.position = position
        self.salary = salary

    def accept(self, visitor):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

class Manager(Employee):
    def __init__(self, name: str, department: str, position: str, salary: float):
        super().__init__(name, department, position, salary)
        self.subordinates: List[Employee] = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

    def accept(self, visitor):
        visitor.visit_manager(self)
        for subordinate in self.subordinates:
            subordinate.accept(visitor)

class RegularEmployee(Employee):
    def __init__(self, name: str, department: str, position: str, salary: float):
        super().__init__(name, department, position, salary)

    def accept(self, visitor):
        visitor.visit_regular_employee(self)

class SalaryReportVisitor:
    def __init__(self):
        self.report = []

    def visit_manager(self, manager: Manager):
        self.report.append(f"Руководитель: {manager.name}, "
                           f"Отдел: {manager.department}, "
                           f"Должность: {manager.position}, "
                           f"Зарплата: ${manager.salary}")

    def visit_regular_employee(self, employee: RegularEmployee):
        self.report.append(f"Сотрудник: {employee.name}, "
                           f"Отдел: {employee.department}, "
                           f"Должность: {employee.position}, "
                           f"Зарплата: ${employee.salary}")

    def generate_report(self) -> str:
        return "\n".join(self.report)

if __name__ == "__main__":
    # Создаем сотрудников
    ceo = Manager("Иван Иванов", "Управление", "Генеральный директор", 10000)
    cto = Manager("Петр Петров", "IT", "Технический директор", 8000)
    dev1 = RegularEmployee("Алексей Сидоров", "IT", "Разработчик", 5000)
    dev2 = RegularEmployee("Мария Кузнецова", "IT", "Разработчик", 5000)
    hr = Manager("Ольга Смирнова", "HR", "Менеджер по персоналу", 7000)
    recruiter = RegularEmployee("Елена Васильева", "HR", "Рекрутер", 4000)

    # Устанавливаем субординацию
    ceo.add_subordinate(cto)
    ceo.add_subordinate(hr)
    cto.add_subordinate(dev1)
    cto.add_subordinate(dev2)
    hr.add_subordinate(recruiter)

    # Создаем посетителя для расчета зарплаты и формирования отчета
    salary_report_visitor = SalaryReportVisitor()

    # Применяем посетителя к CEO
    ceo.accept(salary_report_visitor)

    # Выводим отчет
    print("Отчет по зарплатам:")
    print(salary_report_visitor.generate_report())