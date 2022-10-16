
def combinationSum(candidates, target):

    out = []
    n = len(candidates)

    def dfs (cur, cur_sum, idx):
        if cur_sum > target: return 
        elif cur_sum == target: out.append(cur)
        else: 
            for i in range(idx, n): dfs(cur + [candidates[i]], cur_sum + candidates[i], i) # check every other element

    dfs([],0,0)
    return out