from crud import create_computer, create_employee, create_repair, create_software
from database import SessionLocal

db = SessionLocal()

# Добавляем тестовые данные
employee = create_employee(db, name="Иванов Иван", position="Инженер")
software = create_software(db, name="Windows 11", version="23H2")
computer = create_computer(db, model="Dell XPS", status="active", employee_id=1)
repair = create_repair(db, computer_id=1, issue="Не включается", date="2024-03-01")

db.close()
print("Тестовые данные добавлены!")
