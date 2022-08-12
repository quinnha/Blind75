
def reverseBits(n):
    r = 0

    for i in range(32):
        r <<= 1  #shifting out to the right
        r ^= n&1
        n >>= 1 # shifting n to the left
    return r


print(reverseBits(43261596))
print(reverseBits(22))
