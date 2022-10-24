nums = [int(x) for x in input().split()]
target = int(input())
result = []

found = False
for index, num in enumerate(nums):
    for idx, nr in enumerate(nums):
        if num + nr == target and index != idx:
            result = [index, idx]
            found = True
            break
        else:
            continue
    if found:
        break

print(result)

