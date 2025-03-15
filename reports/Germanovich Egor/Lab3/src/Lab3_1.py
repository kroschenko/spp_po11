class TourPackage:
    def __init__(self):
        self.selected_options = {}
        self.total_cost = 0

    def add_options(self, category: str, options: list, cost: int):
        self.selected_options[category] = options
        self.total_cost += cost

    def __str__(self):
        parts = ["Ваш заказ:"]
        for category, options in self.selected_options.items():
            parts.append(f"{category}: {', '.join(options)}")
        parts.append(f"\nИтоговая стоимость: {self.total_cost} руб.")
        return "\n".join(parts)


class TourPackageBuilder:
    def __init__(self):
        self.tour_package = TourPackage()

    def add_category_options(self, category: str, options: list, cost: int):
        self.tour_package.add_options(category, options, cost)

    def get_result(self) -> TourPackage:
        return self.tour_package


def select_option(category_name: str, options: dict, is_multiple: bool = False):
    print(f"\nВыберите опции для {category_name}:")
    for idx, (option, price) in enumerate(options.items(), 1):
        print(f"{idx}. {option} - {price} руб.")

    while True:
        choice = input("Введите номера через запятую, если несколько: " if is_multiple else "Введите номер: ")
        try:
            selected_indices = list(map(int, choice.split(","))) if is_multiple else [int(choice)]

            if not all(1 <= idx <= len(options) for idx in selected_indices):
                raise ValueError

            selected = []
            total = 0
            for idx in selected_indices:
                option = list(options.keys())[idx - 1]
                price = list(options.values())[idx - 1]
                selected.append(option)
                total += price
            return selected, total

        except (ValueError, IndexError):
            print("Ошибка. Введите правильные номера.")


def main():
    print("Добро пожаловать в Туристическое бюро!\n")

    tour_options = {
        "Транспорт": {"Самолет": 15000, "Поезд": 8000, "Автобус": 5000, "Не включать": 0},
        "Проживание": {"Отель 3*": 3000, "Отель 4*": 5000, "Отель 5*": 8000, "Не включать": 0},
        "Питание": {"Без питания": 0, "Завтрак": 1500, "Полный пансион": 3000},
        "Музеи": {"Музей истории": 500, "Художественная галерея": 700, "Научный музей": 600},
        "Экскурсии": {"Обзорная": 1000, "Тематическая": 1500, "Водная": 2000},
    }

    multiple_choice = ["Музеи", "Экскурсии"]
    builder = TourPackageBuilder()

    for category, options in tour_options.items():
        is_multiple = category in multiple_choice
        selected_opts, cost = select_option(category, options, is_multiple)
        builder.add_category_options(category, selected_opts, cost)

    tour_package = builder.get_result()
    print(tour_package)


if __name__ == "__main__":
    main()
