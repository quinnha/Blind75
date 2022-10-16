
def permute(nums):

    n = len(nums)

    res = []
    def dfs(path, used, res):
        if len(path) == n: 
            res.append(path[:])
            return
        else:
            for i, num in enumerate(nums):
                if used[i]: continue # check if element was used
                used[i] = True
                path.append(num)
                dfs(path, used, res)
                used[i] = False
                path.pop()

    dfs([], [False] * n, res)
    return res

print(permute([1,2,3]))