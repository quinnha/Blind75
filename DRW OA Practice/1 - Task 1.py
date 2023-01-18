# Find Missing Observations - https://leetcode.com/problems/find-missing-observations/description/
def solution(A, F, M):
    m = len(A)
    diff = M * (m + F) - sum(A)
    if diff > 6 * F or diff < F:
        return [0]
    div, mod = divmod(diff, F)
    return [div + 1] * mod + [div] * (F - mod)
