"""System administration API for managing users, servers, logs, tasks, and permissions."""

from datetime import datetime

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session

# Настройка SQLAlchemy
engine = create_engine("sqlite:///sysadmin.db", echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# Dependency для работы с базой данных
def get_db():
    """Provide a database session for each request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Настройка FastAPI
app = FastAPI()

# Модели SQLAlchemy для таблиц
class User(Base):
    """SQLAlchemy model for the users table."""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    role = Column(String(50), nullable=False)
    logs = relationship("Log", back_populates="user")
    tasks = relationship("Task", back_populates="user")
    permissions = relationship("Permission", back_populates="user")

class Server(Base):
    """SQLAlchemy model for the servers table."""
    __tablename__ = "servers"
    id = Column(Integer, primary_key=True)
    server_name = Column(String(50), unique=True, nullable=False)
    ip_address = Column(String(15), unique=True, nullable=False)
    status = Column(String(20), nullable=False)
    logs = relationship("Log", back_populates="server")
    tasks = relationship("Task", back_populates="server")
    permissions = relationship("Permission", back_populates="server")

class Log(Base):
    """SQLAlchemy model for the logs table."""
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    server_id = Column(Integer, ForeignKey("servers.id"), nullable=False)
    log_message = Column(String(200), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="logs")
    server = relationship("Server", back_populates="logs")

class Task(Base):
    """SQLAlchemy model for the tasks table."""
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    server_id = Column(Integer, ForeignKey("servers.id"), nullable=False)
    task_description = Column(String(200), nullable=False)
    status = Column(String(20), nullable=False)
    user = relationship("User", back_populates="tasks")
    server = relationship("Server", back_populates="tasks")

class Permission(Base):
    """SQLAlchemy model for the permissions table."""
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    server_id = Column(Integer, ForeignKey("servers.id"), nullable=False)
    permission_level = Column(String(20), nullable=False)
    user = relationship("User", back_populates="permissions")
    server = relationship("Server", back_populates="permissions")

# Создание таблиц в базе данных
Base.metadata.create_all(engine)

# Модели Pydantic для FastAPI
class UserCreate(BaseModel):
    """Pydantic model for creating a user."""
    username: str
    email: str
    role: str

class ServerCreate(BaseModel):
    """Pydantic model for creating a server."""
    server_name: str
    ip_address: str
    status: str

class LogCreate(BaseModel):
    """Pydantic model for creating a log."""
    user_id: int
    server_id: int
    log_message: str

class TaskCreate(BaseModel):
    """Pydantic model for creating a task."""
    user_id: int
    server_id: int
    task_description: str
    status: str

class PermissionCreate(BaseModel):
    """Pydantic model for creating a permission."""
    user_id: int
    server_id: int
    permission_level: str

# Эндпойнты FastAPI
# CRUD для пользователей
@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user in the database."""
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    """Retrieve a user by ID."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    """Update a user's details."""
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Delete a user by ID."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    db.delete(user)
    db.commit()
    return {"message": "Пользователь удалён"}

# CRUD для серверов
@app.post("/servers/")
def create_server(server: ServerCreate, db: Session = Depends(get_db)):
    """Create a new server in the database."""
    db_server = Server(**server.dict())
    db.add(db_server)
    db.commit()
    db.refresh(db_server)
    return db_server

@app.get("/servers/{server_id}")
def read_server(server_id: int, db: Session = Depends(get_db)):
    """Retrieve a server by ID."""
    server = db.query(Server).filter(Server.id == server_id).first()
    if not server:
        raise HTTPException(status_code=404, detail="Сервер не найден")
    return server

@app.put("/servers/{server_id}")
def update_server(server_id: int, server: ServerCreate, db: Session = Depends(get_db)):
    """Update a server's details."""
    db_server = db.query(Server).filter(Server.id == server_id).first()
    if not db_server:
        raise HTTPException(status_code=404, detail="Сервер не найден")
    for key, value in user.dict().items():
        setattr(db_server, key, value)
    db.commit()
    db.refresh(db_server)
    return db_server

@app.delete("/servers/{server_id}")
def delete_server(server_id: int, db: Session = Depends(get_db)):
    """Delete a server by ID."""
    server = db.query(Server).filter(Server.id == server_id).first()
    if not server:
        raise HTTPException(status_code=404, detail="Сервер не найден")
    db.delete(server)
    db.commit()
    return {"message": "Сервер удалён"}

# CRUD для логов
@app.post("/logs/")
def create_log(log: LogCreate, db: Session = Depends(get_db)):
    """Create a new log entry in the database."""
    db_log = Log(**log.dict(), timestamp=datetime.utcnow())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

@app.get("/logs/{log_id}")
def read_log(log_id: int, db: Session = Depends(get_db)):
    """Retrieve a log by ID."""
    log = db.query(Log).filter(Log.id == log_id).first()
    if not log:
        raise HTTPException(status_code=404, detail="Лог не найден")
    return log

@app.put("/logs/{log_id}")
def update_log(log_id: int, log: LogCreate, db: Session = Depends(get_db)):
    """Update a log's details."""
    db_log = db.query(Log).filter(Log.id == log_id).first()
    if not db_log:
        raise HTTPException(status_code=404, detail="Лог не найден")
    for key, value in log.dict().items():
        setattr(db_log, key, value)
    db.commit()
    db.refresh(db_log)
    return db_log

@app.delete("/logs/{log_id}")
def delete_log(log_id: int, db: Session = Depends(get_db)):
    """Delete a log by ID."""
    log = db.query(Log).filter(Log.id == log_id).first()
    if not log:
        raise HTTPException(status_code=404, detail="Лог не найден")
    db.delete(log)
    db.commit()
    return {"message": "Лог удалён"}

# CRUD для задач
@app.post("/tasks/")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """Create a new task in the database."""
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/{task_id}")
def read_task(task_id: int, db: Session = Depends(get_db)):
    """Retrieve a task by ID."""
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    """Update a task's details."""
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    for key, value in task.dict().items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """Delete a task by ID."""
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    db.delete(task)
    db.commit()
    return {"message": "Задача удалена"}

# CRUD для прав доступа
@app.post("/permissions/")
def create_permission(permission: PermissionCreate, db: Session = Depends(get_db)):
    """Create a new permission in the database."""
    db_permission = Permission(**permission.dict())
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission

@app.get("/permissions/{permission_id}")
def read_permission(permission_id: int, db: Session = Depends(get_db)):
    """Retrieve a permission by ID."""
    permission = db.query(Permission).filter(Permission.id == permission_id).first()
    if not permission:
        raise HTTPException(status_code=404, detail="Право доступа не найдено")
    return permission

@app.put("/permissions/{permission_id}")
def update_permission(permission_id: int, permission: PermissionCreate, db: Session = Depends(get_db)):
    """Update a permission's details."""
    db_permission = db.query(Permission).filter(Permission.id == permission_id).first()
    if not db_permission:
        raise HTTPException(status_code=404, detail="Право доступа не найдено")
    for key, value in permission.dict().items():
        setattr(db_permission, key, value)
    db.commit()
    db.refresh(db_permission)
    return db_permission

@app.delete("/permissions/{permission_id}")
def delete_permission(permission_id: int, db: Session = Depends(get_db)):
    """Delete a permission by ID."""
    permission = db.query(Permission).filter(Permission.id == permission_id).first()
    if not permission:
        raise HTTPException(status_code=404, detail="Право доступа не найдено")
    db.delete(permission)
    db.commit()
    return {"message": "Право доступа удалено"}
