dict = {}
var = []
term = []

with open('tes.txt') as f:
    list = f.read().splitlines()

print(list)

maxRow = len(list)
for i in range(maxRow):
    maxCol = len(list[i])
    foundKey = False
    foundStart = False
    word = ""
    for j in range(maxCol):
        char = list[i][j]
        if (not(foundKey)):
            if (char == ' '):
                foundKey = True
                key = word
                dict[key] = []
                word = char
            else:
                word += char
        elif (not(foundStart)):
            word += char
            if (word == " => "):
                foundStart = True
                dict[key].append([])
                prod = 0
                word = ""
        else:
            foundVal = False
            if (not(foundVal)):
                if (char != ' ') & (char != '|'):
                    word += char
                if (char == ' ') | (char == '|') | (j == maxCol-1):
                    foundVal = True
                    val = word
                    word = ""
            if (foundVal):
                if (val != ""):
                    dict[key][prod].append(val)
                    if (len(val) > 1):
                        var.append(val)
                    else:
                        if (val.isupper()):
                            var.append(val)
                        else:
                            term.append(val)
                elif (val == ""):
                    if (char == '|'):
                        dict[key].append([])
                        prod += 1

# i = 1
# for key, value in dict.items():
#     print(f"Produksi ke-{i}:")
#     print(f"{key} : {value}")
#     i += 1

print(var)
print(term)