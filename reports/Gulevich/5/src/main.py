from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from crud import (
    create_computer,
    create_employee,
    create_repair,
    create_software,
    get_computer,
)
from database import SessionLocal
from schemas import ComputerCreate, EmployeeCreate, RepairCreate, SoftwareCreate

app = FastAPI()


# Зависимость для сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Эндпоинты для Computers
@app.post("/computers/", response_model=ComputerCreate)
def add_computer(computer: ComputerCreate, db: Session = Depends(get_db)):
    return create_computer(db, **computer.dict())


@app.get("/computers/{computer_id}")
def read_computer(computer_id: int, db: Session = Depends(get_db)):
    db_computer = get_computer(db, computer_id)
    if not db_computer:
        raise HTTPException(status_code=404, detail="Computer not found")
    return db_computer


# Эндпоинты для Software
@app.post("/software/", response_model=SoftwareCreate)
def add_software(software: SoftwareCreate, db: Session = Depends(get_db)):
    return create_software(db, **software.dict())


# Эндпоинты для Employees
@app.post("/employees/", response_model=EmployeeCreate)
def add_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(db, **employee.dict())


# Эндпоинты для Repairs
@app.post("/repairs/", response_model=RepairCreate)
def add_repair(repair: RepairCreate, db: Session = Depends(get_db)):
    return create_repair(db, **repair.dict())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
