import re
import copy

def solution(expression):
    comb = [('-','+','*'),('-','*','+'),('+','-','*'),('+','*','-'),('*','-','+'),('*','+','-')]
    num_list = re.split('[-+*]', expression)
    opr_list = []
    exp_list = []
    values = []

    for i in expression:
        if i in '-+*':
            opr_list.append(i)

    for i in range(len(num_list)):
        if num_list:
            exp_list.append(num_list.pop(0))
        if opr_list:
            exp_list.append(opr_list.pop(0))

    for (i, j, k) in comb:
        temp = copy.deepcopy(exp_list)
        # print('##### {} > {} > {} #####'.format(i, j, k))
        for opr in [i, j, k]:
            idx = 0
            while idx < len(temp):
                if temp[idx] == opr:
                    res = eval(temp[idx-1] + opr+ temp[idx+1])
                    temp.pop(idx-1)
                    temp.pop(idx-1)
                    temp.pop(idx-1)
                    temp.insert(idx-1, str(res))
                    print(temp)
                else:
                    idx += 1
        value = abs(int(temp[0]))
        # print('Result: ', value)
        values.append(value)

    return max(values)