from dataclasses import dataclass

@dataclass
class Const:
    DATABASE_URL: str = "sqlite:///./computer_build.db"
