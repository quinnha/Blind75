
def reverseBits(n):
    r = 0

    for i in range(32):
        r <<= 1  #shifting out to the left (adds a 0 to the right, perfect for xor)
        r ^= n&1 # "adding" the bit to the output (0 if 0 1 if 1)
        n >>= 1 # shifting n to the left, looking at next bit
    return r


print(reverseBits(43261596))

# xor is like the addition of bits just doesnt account for carry