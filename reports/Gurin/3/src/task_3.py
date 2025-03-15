from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class ReadFileCommand(Command):
    def __init__(self, filepath):
        self.filepath = filepath
        self.content = None

    def execute(self):
        with open(self.filepath, "r", encoding="utf-8") as file:
            self.content = file.read()
        print(f"Прочитан файл: {self.filepath}")
        return self.content

    def undo(self):
        print("Операция чтения файла не требует отмены.")


class ReadMultipleFilesCommand(Command):
    def __init__(self, filepaths):
        self.filepaths = filepaths
        self.contents = {}

    def execute(self):
        for filepath in self.filepaths:
            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    self.contents[filepath] = file.read()
                print(f"Прочитан файл: {filepath}")
            except FileNotFoundError:
                print(f"Файл {filepath} не найден.")
        return self.contents

    def undo(self):
        print("Операция чтения файлов не требует отмены.")


class WriteFileCommand(Command):
    def __init__(self, filepath, content):
        self.filepath = filepath
        self.content = content
        self.previous_content = None

    def execute(self):
        with open(self.filepath, "r", encoding="utf-8") as file:
            self.previous_content = file.read()
        with open(self.filepath, "w", encoding="utf-8") as file:
            file.write(self.content)
        print(f"Файл {self.filepath} изменен.")

    def undo(self):
        with open(self.filepath, "w", encoding="utf-8") as file:
            file.write(self.previous_content)
        print(f"Изменения в файле {self.filepath} отменены.")


class FileManager:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        result = command.execute()
        self.history.append(command)
        return result

    def undo_last_command(self):
        if self.history:
            command = self.history.pop()
            command.undo()
        else:
            print("Нет операций для отмены.")


def main():
    manager = FileManager()

    read_command = ReadFileCommand("example.txt")
    content = manager.execute_command(read_command)
    print(content)

    read_multiple_files_command = ReadMultipleFilesCommand(["example.txt", "example2.txt"])
    contents = manager.execute_command(read_multiple_files_command)
    for filepath, content in contents.items():
        print(f"Содержимое файла {filepath}:")
        print(content)

    write_command = WriteFileCommand("example.txt", "Новое содержимое файла.")
    manager.execute_command(write_command)

    content = manager.execute_command(read_command)
    print(content)

    manager.undo_last_command()


if __name__ == "__main__":
    main()
