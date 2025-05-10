from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from const import Const

# Создаем движок для работы с базой данных
engine = create_engine(Const.DATABASE_URL, connect_args={"check_same_thread": False})

# Создаем локальную сессию для работы с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()

# Функция для инициализации базы данных
def init_db():
    Base.metadata.create_all(bind=engine)
    