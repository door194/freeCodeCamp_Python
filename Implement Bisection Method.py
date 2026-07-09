def square_root_bisection(sqrt_num, tolerance=0.01, max_iter=100):
    if sqrt_num < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if sqrt_num == 0 or sqrt_num == 1:
        print(f"The square root of {sqrt_num} is {sqrt_num}")
        return sqrt_num

    low = 0
    high = max(1, sqrt_num)

    for _ in range(max_iter):
        guess = (low + high) / 2

        if (high - low) <= tolerance:
            print(f"The square root of {sqrt_num} is approximately {guess}")
            return guess

        if guess * guess < sqrt_num:
            low = guess
        else:
            high = guess

    print(f"Failed to converge within {max_iter} iterations")
    return None
