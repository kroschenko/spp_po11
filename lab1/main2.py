def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False
    
def main():
    num = int(input('Введите число: '))
    print(isPalindrome(num))
    
if __name__ == "__main__":
    main()
    