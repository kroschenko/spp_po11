def find_unique_numbers(numbers_list: list):
    if not isinstance(numbers_list, list):
        raise TypeError("Input must be a list.")

    for num in numbers_list:
        if not isinstance(num, int):
            raise TypeError("All elements in the list must be integers.")
    return set(numbers_list)


if __name__ == "__main__":
    amount_of_numbers: int = int(input("Enter amount of numbers: "))
    user_numbers: list = []

    for _ in range(amount_of_numbers):
        number = int(input("Enter number: "))
        user_numbers.append(number)
    print("Unique numbers: ", find_unique_numbers(user_numbers))
