from collections import Counter


def isInterleave(s1, s2, s3):
    f1 = Counter(s1)
    f2 = Counter(s2)
    f3 = Counter(s3)

    for key in f3.keys():
        if f1[key] + f2[key] != f3[key]:
            return False

    return True


# is incorrect -> not sure what the question is asking
