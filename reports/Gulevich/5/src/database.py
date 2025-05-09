from sqlalchemy import Column, ForeignKey, Integer, String, Table, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# Таблица для связи многие-ко-многим (Компьютеры <-> ПО)
computer_software = Table(
    "computer_software",
    Base.metadata,
    Column("computer_id", Integer, ForeignKey("computers.id")),
    Column("software_id", Integer, ForeignKey("software.id")),
)


class Computer(Base):
    __tablename__ = "computers"
    id = Column(Integer, primary_key=True)
    model = Column(String(50), nullable=False)
    status = Column(String(20))  # active, broken, archived
    employee_id = Column(Integer, ForeignKey("employees.id"))
    repairs = relationship("Repair", backref="computer")
    software = relationship("Software", secondary=computer_software)


class Software(Base):
    __tablename__ = "software"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    version = Column(String(20))


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    position = Column(String(30))
    computers = relationship("Computer", backref="employee")


class Repair(Base):
    __tablename__ = "repairs"
    id = Column(Integer, primary_key=True)
    computer_id = Column(Integer, ForeignKey("computers.id"))
    issue = Column(String(200))
    date = Column(String(10))  # Формат: YYYY-MM-DD


# Подключение к SQLite
engine = create_engine("sqlite:///computer_lab.db", echo=True)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)
