from collections import deque

roman_symbols = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000}

numbers = deque(list(input()))
result = 0
while True:
    if not numbers:
        break
    first_num = numbers.popleft()
    if numbers and first_num == "I":
        if numbers[0] == "V":
            result += 4
            numbers.popleft()
            continue

        elif numbers[0] == "X":
            result += 9
            numbers.popleft()
            continue

        else:
            result += roman_symbols[first_num]
            continue

    elif numbers and first_num == "X":
        if numbers[0] == "L":
            result += 40
            numbers.popleft()
            continue

        elif numbers[0] == "C":
            result += 90
            numbers.popleft()
            continue

        else:
            result += roman_symbols[first_num]
            continue

    elif numbers and first_num == "C":
        if numbers[0] == "D":
            result += 400
            numbers.popleft()
            continue

        elif numbers[0] == "M":
            result += 900
            numbers.popleft()
            continue

        else:
            result += roman_symbols[first_num]
            continue
    result += roman_symbols[first_num]

print(result)
