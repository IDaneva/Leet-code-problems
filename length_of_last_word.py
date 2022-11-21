def lengthOfLastWord( s):
    """
    :type s: str
    :rtype: int
    """
    s = s.split()
    return len(s[-1])