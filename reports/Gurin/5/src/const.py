from dataclasses import dataclass


@dataclass
class Const:
    DATABASE_URL: str = "sqlite:///./university_schedule.db"
