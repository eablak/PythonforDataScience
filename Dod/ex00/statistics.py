def calculate_mean(numbers:  list):
    print("mean : ", sum(numbers) / len(numbers))


def calculate_median(numbers: list):
    numbers.sort()
    median = 0
    n = len(numbers)
    
    if len(numbers) % 2 != 0:
        median = numbers[(n - 1) // 2]
    else:
        median = numbers[(n-1) // 2] + numbers[n//2]
    
    print("median : ", median)


def calculate_quartile(numbers: list):
    n = len(numbers)
    numbers.sort()
    quartile = []

    print((n - 1) * 0.25 + 1)

    # quartile.append(numbers[(n - 1) * 0.25 + 1])
    # quartile.append(numbers[(n - 1) * 0.75 + 1])
    
    # print("quartile : ",quartile)


def ft_statistics(*args: any, **kwargs: any) -> None:
    
    for k, val in kwargs.items():
        if val == "mean":
            calculate_mean(list(args))
        elif val == "median":
            calculate_median(list(args))
        elif val == "quartile":
            calculate_quartile(list(args))

