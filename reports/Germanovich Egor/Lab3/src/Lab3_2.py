from abc import ABC, abstractmethod
from datetime import datetime


class FileSystemComponent(ABC):
    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def display(self, indent: str = "") -> str:
        pass


class File(FileSystemComponent):
    def __init__(self, name: str, size: int, extension: str, created: datetime):
        self.name = name
        self.size = size
        self.extension = extension
        self.created = created

    def get_size(self) -> int:
        return self.size

    def display(self, indent: str = "") -> str:
        return f"{indent}📄 {self.name}.{self.extension} (Size: {self.size} bytes, Created: {self.created.strftime('%Y-%m-%d %H:%M:%S')})"


class Directory(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def get_size(self) -> int:
        return sum(child.get_size() for child in self.children)

    def display(self, indent: str = "") -> str:
        result = f"{indent}📁 {self.name} (Size: {self.get_size()} bytes)\n"
        for child in self.children:
            result += child.display(indent + "  ") + "\n"
        return result.rstrip()


def create_file():
    name = input("Введите имя файла: ")
    size = int(input("Введите размер файла (в байтах): "))
    extension = input("Введите расширение файла (например, txt, jpg): ")
    created = datetime.now()
    return File(name, size, extension, created)


def create_directory():
    name = input("Введите имя директории: ")
    return Directory(name)


def main():
    root = Directory("Root")
    while True:
        print("\nМеню:")
        print("1. Добавить файл")
        print("2. Добавить директорию")
        print("3. Показать структуру файловой системы")
        print("4. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            file = create_file()
            current = root
            while True:
                print(f"\nТекущая директория: {current.name}")
                print("Доступные поддиректории:")
                for i, child in enumerate(current.children):
                    if isinstance(child, Directory):
                        print(f"{i + 1}. 📁 {child.name}")
                print(f"{len(current.children) + 1}. Добавить в текущую директорию")
                dir_choice = input("Выберите директорию или добавьте в текущую: ")
                if dir_choice.isdigit() and 1 <= int(dir_choice) <= len(current.children):
                    current = current.children[int(dir_choice) - 1]
                else:
                    current.add(file)
                    break
        elif choice == "2":
            directory = create_directory()
            current = root
            while True:
                print(f"\nТекущая директория: {current.name}")
                print("Доступные поддиректории:")
                for i, child in enumerate(current.children):
                    if isinstance(child, Directory):
                        print(f"{i + 1}. 📁 {child.name}")
                print(f"{len(current.children) + 1}. Добавить в текущую директорию")
                dir_choice = input("Выберите директорию или добавьте в текущую: ")
                if dir_choice.isdigit() and 1 <= int(dir_choice) <= len(current.children):
                    current = current.children[int(dir_choice) - 1]
                else:
                    current.add(directory)
                    break
        elif choice == "3":
            print("\nСтруктура файловой системы:")
            print(root.display())
        elif choice == "4":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
