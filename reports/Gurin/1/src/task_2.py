def binary_addition(*nums) -> str:
    _sum: int = 0
    for _ in nums:
        if _ < 0:
            raise TypeError("Negative numbers are not supported.")
        _sum += _
    return bin(_sum)[2:]


if __name__ == "__main__":
    number_1: int = int(input("Enter the first binary number: "), 2)
    number_2: int = int(input("Enter the second binary number: "), 2)
    result: str = binary_addition(number_1, number_2)
    print(result)
