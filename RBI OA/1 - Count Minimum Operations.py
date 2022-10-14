def countMinimumOperations(password):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    v = ""
    c = ""

    if len(password) == 0: return 0

    # check if we are chilling
    for char in password:
        if char in vowels:
            vowel_count += 1
            v += char
        else:
            consonant_count += 1
            c += char
    if vowel_count == consonant_count:
        return 0
    num_loop = int(abs(vowel_count - consonant_count)/2)
    out = 0
    if vowel_count > consonant_count:
        return num_loop
    else:
        rank_1 = "bdfhjnptv"
        rank_2 = "cgkmqsw"
        rank_3 = "lrx"
        rank_4 = "y"
        rank_5 = "z"
        c_list = [0] * len(c)
        for i in range(len(c)):
            if c[i] in rank_1:
                c_list[i] = 1
            elif c[i] in rank_2:
                c_list[i] = 2
            elif c[i] in rank_3:
                c_list[i] = 3
            elif c[i] in rank_4:
                c_list[i] = 4
            else:
                c_list[i] = 5
        c_list.sort()
        
        for i in range(num_loop):
            print (c_list[i])
            out += c_list[i]
        return out


            
print(countMinimumOperations("bigbangt"))
    