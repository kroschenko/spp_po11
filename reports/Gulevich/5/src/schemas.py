from pydantic import BaseModel


class ComputerCreate(BaseModel):
    model: str
    status: str
    employee_id: int


class SoftwareCreate(BaseModel):
    name: str
    version: str


class EmployeeCreate(BaseModel):
    name: str
    position: str


class RepairCreate(BaseModel):
    computer_id: int
    issue: str
    date: str
