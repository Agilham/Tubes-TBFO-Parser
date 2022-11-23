def getCFG():
    produksi = dict()
    variabel = set()
    terminal = set()
    with open('tes.txt') as f:
        list = f.read().splitlines()
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
                    produksi[key] = set()
                    word = char
                else:
                    word += char
            elif (not(foundStart)):
                word += char
                if (word == " => "):
                    foundStart = True
                    RHS = []
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
                        RHS.append(val)
                        if (len(val) > 1):
                            variabel.add(val)
                        else:
                            terminal.add(val)
                    else:
                        if (char == '|'):
                            produksi[key].add(tuple(RHS))
                            RHS = []
    return produksi, variabel, terminal