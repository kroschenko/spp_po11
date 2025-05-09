from typing import List


class Employee:
    def __init__(self, name: str, department: str, position: str, salary: float):
        self.name = name
        self.department = department
        self.position = position
        self.salary = salary

    def add_subordinate(self, employee):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

    def remove_subordinate(self, employee):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

    def get_subordinates(self) -> List["Employee"]:
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

    def __str__(self):
        return (
            f"Сотрудник: {self.name}, "
            f"Отдел: {self.department}, "
            f"Должность: {self.position}, "
            f"Зарплата: ${self.salary}"
        )


class Manager(Employee):
    def __init__(self, name: str, department: str, position: str, salary: float):
        self.subordinates: List[Employee] = []
        super().__init__(name, department, position, salary)

    def add_subordinate(self, employee: "Employee"):
        self.subordinates.append(employee)
        print(f"{employee.name} теперь подчиняется {self.name}")

    def remove_subordinate(self, employee: "Employee"):
        if employee in self.subordinates:
            self.subordinates.remove(employee)
            print(f"{employee.name} больше не подчиняется {self.name}")
        else:
            print(f"{employee.name} не найден в подчинении у {self.name}")

    def get_subordinates(self) -> List["Employee"]:
        return self.subordinates

    def __str__(self):
        subordinates_info = "\n  ".join([str(sub) for sub in self.subordinates])
        return (
            f"{super().__str__()}\n"
            f"Подчиненные:\n  {subordinates_info if subordinates_info else 'Нет подчиненных'}"
        )


class RegularEmployee(Employee):
    def __init__(self, name: str, department: str, position: str, salary: float):
        Employee.__init__(self, name, department, position, salary)

    def add_subordinate(self, employee):
        print("Обычные сотрудники не могут иметь подчиненных")

    def remove_subordinate(self, employee):
        print("Обычные сотрудники не могут иметь подчиненных")

    def get_subordinates(self) -> List["Employee"]:
        return []

    def __str__(self):
        return Employee.__str__(self)


if __name__ == "__main__":
    ceo = Manager("Иван Иванов", "Управление", "Генеральный директор", 10000)
    cto = Manager("Петр Петров", "IT", "Технический директор", 8000)
    dev1 = RegularEmployee("Алексей Сидоров", "IT", "Разработчик", 5000)
    dev2 = RegularEmployee("Мария Кузнецова", "IT", "Разработчик", 5000)
    hr = Manager("Ольга Смирнова", "HR", "Менеджер по персоналу", 7000)
    recruiter = RegularEmployee("Елена Васильева", "HR", "Рекрутер", 4000)

    ceo.add_subordinate(cto)
    ceo.add_subordinate(hr)
    cto.add_subordinate(dev1)
    cto.add_subordinate(dev2)
    hr.add_subordinate(recruiter)

    print("\nИнформация о CEO:")
    print(ceo)

    print("\nИнформация о CTO:")
    print(cto)

    print("\nИнформация о HR:")
    print(hr)

    cto.remove_subordinate(dev1)
    print("\nИнформация о CTO после удаления разработчика:")
    print(cto)
