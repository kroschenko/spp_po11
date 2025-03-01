def process_sequence(sequence):
    if not sequence:
        return "The sequence is empty"
    
    max_value = max(sequence)
    min_value = min(sequence)
    sum_value = sum(sequence)
    
    product_value = 1
    for num in sequence:
        product_value *= num
    
    return max_value, min_value, sum_value, product_value


N = int(input("Enter the number of elements in the sequence: "))
sequence = [int(input(f"Enter element {i+1}: ")) for i in range(N)]

max_val, min_val, sum_val, product_val = process_sequence(sequence)

print(f"Maximum value: {max_val}")
print(f"Minimum value: {min_val}")
print(f"Sum of elements: {sum_val}")
print(f"Product of elements: {product_val}")