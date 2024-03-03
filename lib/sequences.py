def generate_fibonacci(length):
    if length == 0:
        return []
    elif length == 1:
        return [0]

    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < length:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)

    return fibonacci_sequence

def print_fibonacci(length):
    fibonacci_sequence = generate_fibonacci(length)
    print(fibonacci_sequence)

# Test the function
print_fibonacci(9)
