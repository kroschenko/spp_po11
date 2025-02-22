def is_valid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            
            top_element = stack.pop() if stack else "#"
           
            if mapping[char] != top_element:
                return False
        else: 
            stack.append(char)

    return not stack


s = input("Введите строку, содержащую только скобки: ")
result = is_valid(s)

print("Результат:", result)
