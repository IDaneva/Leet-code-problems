def remove_duplicates(nums):
    nums = sorted(set(nums))
    return nums


a = remove_duplicates([1, 1, 2])
print(a)
