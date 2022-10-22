#im not going to lie how the hell do you come up with this (non-naive)
# cancelling a 1 every time by comparing n and n-1

# def hammingWeight(n):
#     count = 0
#     while n != 0:
#         n = n&(n-1)
#         count+= 1
    
#     return count

#malding because original sol i came up with woudlve worked in ajva (comparing last bit and left shift)
# but this doesnt work because python wants to be a special snowflake
def hammingWeight(n):
    count = 0
    while n!=0:
        last_dig = int(str(n)[-1])
        count += last_dig & 1
        n >> 1
    return count


