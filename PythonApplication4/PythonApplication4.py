def fibonacci_sequence(n):
    sequence = [0, 1]
    
    while len(sequence) < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    
    return sequence[:n]

n = int(input())
fib_sequence = fibonacci_sequence(n)
print(f"Đầu ra dãy Fibonacci đầu tiên {n} số là: {fib_sequence}")
