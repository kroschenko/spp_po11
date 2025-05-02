from sqlalchemy.orm import Session

from database import Computer, Employee, Repair, Software


# Computers
def create_computer(db: Session, model: str, status: str, employee_id: int):
    db_computer = Computer(model=model, status=status, employee_id=employee_id)
    db.add(db_computer)
    db.commit()
    return db_computer


def get_computer(db: Session, computer_id: int):
    return db.query(Computer).filter(Computer.id == computer_id).first()


# Software
def create_software(db: Session, name: str, version: str):
    db_software = Software(name=name, version=version)
    db.add(db_software)
    db.commit()
    return db_software


# Employees
def create_employee(db: Session, name: str, position: str):
    db_employee = Employee(name=name, position=position)
    db.add(db_employee)
    db.commit()
    return db_employee


# Repairs
def create_repair(db: Session, computer_id: int, issue: str, date: str):
    db_repair = Repair(computer_id=computer_id, issue=issue, date=date)
    db.add(db_repair)
    db.commit()
    return db_repair
