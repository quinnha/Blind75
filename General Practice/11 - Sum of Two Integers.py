# just have to trace it out unfortuantely
# on a bit level, carry = a AND b
# a = a XOR b (adding a and b)
# b shifts the carry left (because when you a and, it stays in place)
# loop quits at b = 0 because that means theres no carry


#note this code does not work in python due to unfixed integer sizes. do this in java lol
def getSum (a,b):

    while b!= 0:
        carry = a&b 
        a = a ^ b 
        b = carry << 1
        print (1)
    return a 

    

print(getSum(1,44))
