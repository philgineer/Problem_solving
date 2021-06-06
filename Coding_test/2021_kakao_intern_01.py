def sol(s):
    res = ''
    length = len(s)
    i = 0
    temp = ''
    num_dict = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    num_list = num_dict.keys()

    while (i < length):
        temp = ''
        if s[i] in '0123456789':
            res += s[i]
            i += 1
        else:
            while s[i] not in '0123456789' and i < length:
                temp += s[i]
                i += 1
                if temp in num_list:
                    break 
        if temp:
            print(temp)
            res += str(num_dict[temp])
    return res

test = 'one4seven89'
print(sol(test))