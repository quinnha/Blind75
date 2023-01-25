def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    split = s.split(" ")
    while split[-1] == "":
        split = split[0:-1]
    return len(split[-1])
    return len(s.strip().split(" ")[-1]) # One liner
