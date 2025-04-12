def find_unique_numbers(listOfNumbers: list):
    if not isinstance(listOfNumbers, list):
        raise TypeError("Input must be a list.")

    for num in listOfNumbers:
        if not isinstance(num, int):
            raise TypeError("All elements in the list must be integers.")
    return set(listOfNumbers)


if __name__ == "__main__":
    amountOfNumbers: int = int(input("Enter amount of numbers: "))
    listOfNumbers: list = []

    for _ in range(amountOfNumbers):
        number = int(input("Enter number: "))
        listOfNumbers.append(number)
    print("Unique numbers: ", find_unique_numbers(listOfNumbers))
