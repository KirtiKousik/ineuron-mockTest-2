def sqrt(x):
    if x < 0:
        raise ValueError("x must be non-negative")

    if x == 0:
        return 0

    start = 0
    end = x
    while start <= end:
        mid = (start + end) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif x < mid * mid:
            end = mid - 1
        else:
            start = mid + 1

    return start

print(sqrt(4))
print(sqrt(8))
print(sqrt(16))
print(sqrt(25))
print(sqrt(36))