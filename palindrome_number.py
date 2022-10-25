x = int(input())


num_as_string = str(x)

if x < 0:
    print("False")
else:
    print(str(x) == str(x)[::-1])

