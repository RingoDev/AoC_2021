with open("input.txt") as file:
    numbers = list(map(int, file.read().split("\n")))
    count_large_than_prev = 0
    prev = None
    for number in numbers:
        if prev is None:
            prev = number
        elif number > prev:
            count_large_than_prev = count_large_than_prev + 1
        prev = number
    print(f"The number increased {count_large_than_prev} times")

## part 2
with open("input.txt") as file:
    numbers = list(map(int, file.read().split("\n")))
    count_large_than_prev = 0
    prev = None
    for i in range(len(numbers) - 2):
        x = sum(numbers[i:i + 3])
        if prev is None:
            prev = x
        elif x > prev:
            count_large_than_prev = count_large_than_prev + 1
        prev = x

    print(f"The number increased {count_large_than_prev} times")
