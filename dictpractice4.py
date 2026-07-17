# COMBINE TWO DICTIONARY BY ADDING


d1 = {10:100 , 20:200 , 30:300 , 40:400}

d2 = {50:500 , 60:600 , 70:700 , 80:800}

for i in d2:

    if i in d1.keys():

        d1[i] += d2[i]

    else:

        d1[i] = d2[i] 

print(i)