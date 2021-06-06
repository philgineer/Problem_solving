croa_list = ['c=','c-','d-', 'dz=','lj','nj','s=','z=']
words = input()
for croa in croa_list:
    words = words.replace(croa, '_')
print(len(words))