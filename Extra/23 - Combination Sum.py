def combinationSum(candidates, target):
    ret = []

    def recurse(build):
        for num in candidates:
            if sum(build) + num < target:
                recurse(build + [num])
            elif sum(build) + num == target:
                if sorted(build + [num]) not in [sorted(val) for val in ret]:
                    ret.append(build + [num])

    for num in candidates:
        if num == target:
            ret.append([num])
        else:
            recurse([num])

    return ret
