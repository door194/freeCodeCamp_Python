def fibonacci(n):
    sequence = [0,1]
    if n < 0:
        return "It should be a positive integer"
    for i in range(2, n+1):
        sequence.append(sequence[i-1] + sequence[i-2])
        print(sequence)
    return sequence[n]

print(fibonacci(2))
