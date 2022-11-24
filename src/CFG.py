class CFG:
    produksii = dict()
    variabeli = set()
    terminali = set()
    
    def readCFG(self,filepath):
        newProduksi = dict()
        newVariabel = set()
        newTerminal = set()
        with open(filepath) as f:
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
                        newProduksi[key] = set()
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
                            if (val == "eps"):
                                val = ""
                            elif (val == "spc"):
                                val = " "
                            RHS.append(val)
                            print(RHS)
                            if (len(val) > 1):
                                newVariabel.add(val)
                            else:
                                newTerminal.add(val)
                            if (j == maxCol-1):
                                newProduksi[key].add(tuple(RHS))
                                RHS = []
                        else:
                            if (char == '|'):
                                newProduksi[key].add(tuple(RHS))
                                RHS = []
            self.produksii = newProduksi
            self.variabeli = newVariabel
            self.terminali = newTerminal

    def print(self):
        print(self.produksii)
        print(self.variabeli)
        print(self.terminali)