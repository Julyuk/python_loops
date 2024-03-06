def factorial_calculator(num):
    if type(num) == int and num >= 0:
        factorial = 1
        if num != 0:
            for i in range(1, num + 1):
                factorial *= i
        print(factorial)
        return factorial
