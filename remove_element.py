def removeElement(nums: list, val: int):
    occurrences = nums.count(val)

    for _ in range(occurrences):
        nums.remove(val)

    return nums


a = removeElement([0,1,2,2,3,0,4,2], 2)
print(a)