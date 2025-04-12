def isPalindrome(x):
    return str(x) == str(x)[::-1]


def main():
    try:
        num = int(input("Введите число: "))
        print(isPalindrome(num))
    except ValueError:
        print(False)


if __name__ == "__main__":
    main()
