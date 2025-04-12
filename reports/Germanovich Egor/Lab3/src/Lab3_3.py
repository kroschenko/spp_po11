import random
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
        date: str = self.created.strftime("%Y-%m-%d %H:%M:%S")
        return f"{indent}📄 {self.name}.{self.extension} (Size: {self.size} bytes, Created: {date})"


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


class DisplayStrategy(ABC):
    @abstractmethod
    def display_components(self, components: list[FileSystemComponent], indent: str = "") -> str:
        pass


class RandomOrderDisplay(DisplayStrategy):
    def display_components(self, components: list[FileSystemComponent], indent: str = "") -> str:
        random.shuffle(components)
        result = ""
        for component in components:
            result += component.display(indent) + "\n"
        return result.rstrip()


class DirectoryWithStrategy(Directory):
    def __init__(self, name: str, display_strategy: DisplayStrategy):
        super().__init__(name)
        self.display_strategy = display_strategy

    def display(self, indent: str = "") -> str:
        result = f"{indent}📁 {self.name} (Size: {self.get_size()} bytes)\n"
        result += self.display_strategy.display_components(self.children, indent + "  ")
        return result


def create_file():
    name = input("Введите имя файла: ")
    size = int(input("Введите размер файла (в байтах): "))
    extension = input("Введите расширение файла (например, txt, jpg): ")
    created = datetime.now()
    return File(name, size, extension, created)


def create_directory():
    name = input("Введите имя директории: ")
    return DirectoryWithStrategy(name, RandomOrderDisplay())


def add_component_to_directory(current, component):
    while True:
        print(f"\nТекущая директория: {current.name}")
        print("Доступные поддиректории:")
        for i, child in enumerate(current.children):
            if isinstance(child, DirectoryWithStrategy):
                print(f"{i + 1}. 📁 {child.name}")
        print(f"{len(current.children) + 1}. Добавить в текущую директории или добавьте в текущую: ")
        dir_choice = input("Выберите директорию или добавьте в текущую: ")
        if dir_choice.isdigit() and 1 <= int(dir_choice) <= len(current.children):
            current = current.children[int(dir_choice) - 1]
        else:
            current.add(component)
            break


def main():
    root = DirectoryWithStrategy("Root", RandomOrderDisplay())
    while True:
        print("\nМеню:")
        print("1. Добавить файл")
        print("2. Добавить директорию")
        print("3. Показать структуру файловой системы")
        print("4. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            file = create_file()
            add_component_to_directory(root, file)
        elif choice == "2":
            directory = create_directory()
            add_component_to_directory(root, directory)
        elif choice == "3":
            print("\nСтруктура файловой системы:")
            print(root.display())
        elif choice == "4":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
