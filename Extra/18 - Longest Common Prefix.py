def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        min_len = min(strs, key = len)
        l = 0
        h = len(min_len)

        while l <= h:
            m = (h + l)//2

            if isCommonPrefix(strs, m):
                l = m + 1
            else:
                h = m - 1
        return strs[0][0:(l + h)/2]


def isCommonPrefix(strs, len):
    sub_string = strs[0][0:len]
    for string in strs:
        if string[0:len] != sub_string: return False
    return True