def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False
    
def main():
    try:
        num = int(input('Введите число: '))
        print(isPalindrome(num))
    except:
        print(False)
if __name__ == "__main__":
    main()
    