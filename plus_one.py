def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    number = int("".join([str(x) for x in digits])) + 1
    return list(str(number))

a = plusOne([1,2,3])
print(a)