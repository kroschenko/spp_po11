def process_sequence(seq):
    if not seq:
        return "The sequence is empty"

    max_value = max(seq)
    min_value = min(seq)
    sum_value = sum(seq)

    product_value = 1
    for num in seq:
        product_value *= num

    return max_value, min_value, sum_value, product_value


if __name__ == "__main__":
    N = int(input("Enter the number of elements in the sequence: "))
    sequence = [int(input(f"Enter element {i+1}: ")) for i in range(N)]

    max_val, min_val, sum_val, product_val = process_sequence(sequence)

    print(f"Maximum value: {max_val}")
    print(f"Minimum value: {min_val}")
    print(f"Sum of elements: {sum_val}")
    print(f"Product of elements: {product_val}")
