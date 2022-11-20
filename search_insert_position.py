def searchInsert(nums: list, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)


a = searchInsert([-3,6,7,8, 10], 0)
print(a)