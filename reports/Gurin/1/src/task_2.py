
def binary_addition(*nums) -> str:
    sum: int = 0
    for _ in nums:
        sum += _
    return bin(sum)[2:]

number_1: int = int(input("Enter the first binary number: "), 2)
number_2: int = int(input("Enter the second binary number: "), 2)
result: str = binary_addition(number_1, number_2)
print(result)
