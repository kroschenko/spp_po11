
amountOfNumbers: int = int(input("Enter amount of numbers: "))
listOfNumbers: list = []

for _ in range(amountOfNumbers):
    number = int(input("Enter number: "))
    listOfNumbers.append(number)

print("Unique numbers: ", set(listOfNumbers))