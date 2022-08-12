#lightweight with python funcitons
# def countBits(n):

#     r = []
#     for i in range(n+1):
#         count = 0

#         r.append(bin(i).count("1"))
        
#     return r

# better sol with bit shifting -> take 12 and apply in a loop, no need to convert to bin since python will jsut do it
def countBits(n):
    r = []
    for i in range (n+1):
        count = 0
        while i !=0:
            i = i &(i-1)
            count +=1
        r.append(count)
    return r


print(countBits(2))





