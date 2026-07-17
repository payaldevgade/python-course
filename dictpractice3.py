# FREQUENCY NUMBER IN DICT
a = [1,1,1,2,2,2,3,5,6,4,7,5,4,3]

d = {}

for i in a:

    if i in d.keys():

        d[i] += 1

    else:

        d[i] = 1
        

print(d)        