def getCombinationOfNullable(RHS, nullable):
    newProduct = set()
    if (len(RHS) != 0):
        combTail = getCombinationOfNullable(RHS[1:],nullable)
        if RHS[0] in nullable:
            newProduct = newProduct.union(combTail)
        for comb in combTail:
            newProduct.add((RHS[0],)+comb)
    else:
        newProduct.add(tuple())
    return newProduct
class test:
    x = 5

def changeVal(t, new):
    t.x = new    

wow = test()
print(wow.x)
changeVal(wow,10)
print(wow.x)
