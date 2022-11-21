dict = {}

with open('tes.txt') as f:
    list = f.read().splitlines()

for i in range(len(list)):
    for j in range(len(list[i])):
        if (j == 0):
            key = list[i][j]
            dict[key] = []
        elif (j == 2):
            dict[key].append([])
            k = 0
        elif (j > 2):
            val = list[i][j]
            newProd = False
            if (val == '|'):
                newProd = True
            if (newProd):
                dict[key].append([])
                k += 1
            elif (val != '|'):
                dict[key][k].append(val)

print(dict)