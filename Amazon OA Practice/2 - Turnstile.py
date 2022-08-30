# From here: https://leetcode.com/discuss/interview-question/699973/goldman-sachs-oa-turnstile

def getTimes(time, direction):

    counter = 0
    check = 0
    out = [0] * len(time)
    en = 0
    ex = 0
    #store the indices of people entering and exiting and time
    enter = []
    exit = []
    for i in range(len(time)):
        if direction[i] == 0: enter = enter.append([i, time[i]])
        else: exit = exit.append([i, time[i]])
    
    # sort by the time that people are entering and exiting
    enter = enter.sort(key = lambda x: x[1])
    exit = exit.sort(key = lambda x: x[1])

    # finally go through all the people
    while True:

        if enter[en][1] < exit[ex][1]: 
            out[i] = counter 
            en += 1
        elif enter[i][1] > exit[i][1]: 
            out[i] = counter 
            ex += 1
        else: 
            out[i] = counter 

        if en == len(enter) or ex == len(exit): break

    return out


print(getTimes([0,0,1,5], [0,1,1,0]))