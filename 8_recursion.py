# CALL stack methods
def func3():
    print("three")


def func2():
    func3()
    print("two")


def fun1():
    func2()
    print("one")


# Recursive function example through Factorial


def factorial(n):
    if n == 1:
        return n
    # print("cal", n * (n - 1))
    return n * factorial(n - 1)


def fibonacci(n):
   # print(n)
    if n == 1 or n == 2:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

# Iterative function example through Factorial


def fibno(n):
    a = 0
    b = 1

    if n < 0:
        return False
    arr = []
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        arr.append(c)
       # print(c)
    print(sum(arr))


def facto(n):
    for i in range(n-1, 0, -1):
        print(i)
        c = n * i
        n = c
    return c
