def fibonacci(n):
    f = [0, 1]  # taking two fibonacci numbers as 0 & 1
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f


result = fibonacci(9)
print(result)
