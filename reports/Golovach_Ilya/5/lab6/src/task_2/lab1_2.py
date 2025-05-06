def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = ""
    for chars in zip(*strs):
        if len(set(chars)) == 1:
            prefix += chars[0]
        else:
            break
    return prefix

def main():
    user_input = input("Введите строки через пробел: ")
    strings_list = list(map(str, user_input.split()))
    print(longest_common_prefix(strings_list))

if __name__ == "__main__":
    main()
