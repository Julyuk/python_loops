def fibonacci_printer(end):
    if type(end) == int and end >= 0:
        start1 = 0
        start2 = 1
        print(start1)
        print(start2)
        fibo = start1 + start2
        for i in range(end):
            fibo = start1 + start2
            if fibo > end:
                break;
            print(fibo)
            start1 = start2
            start2 = fibo
    else:
        raise ValueError("End number must be 0 or a positive integer")
