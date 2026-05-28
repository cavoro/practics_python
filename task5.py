def climb_recursive(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    return climb_recursive(n - 1) + climb_recursive(n - 2)


def climb_iterative(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    a = 1
    b = 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


values = [10, 20, 30]

for n in values:
    print(climb_recursive(n))
    print(climb_iterative(n))
