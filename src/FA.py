lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
otherSym = "._()"
operator = "+-*/"

def FAvariabel(input):
    transisi = {'q0' : {('_','q1'),('$','q1'),(lowercase,'q1')},
                'q1' : {('_','q1'),('$','q1'),(lowercase,'q1'),(uppercase,'q1')}}
    finalState = set(['q0','q1'])
    i = 0
    state = 'q0'
    while (i < len(input)):
        found = False
        for trans in transisi[state]:
            for i in range(len(trans[0])):
                if (input[i] == trans[0][i]):
                    state = trans[1]
                    found = True
        if (found):
            i += 1
        else:
            break
    if (i == len(input) and state in finalState):
        return True
    else:
        return False
    
def FAoperasi(input):
    # belum seleai
    transisi = {'q0' : {(' ','q0'),('-','q2'),('!','q2'),(lowercase+uppercase+otherSym+number,'q1')},
    'q1' : {(lowercase+uppercase+otherSym+number,'q1'),('$','q1'),(lowercase,'q1'),(uppercase,'q1'),(operator,'q2')},
    'q2' : {(lowercase+uppercase+otherSym+number,'q3')},
    'q3' : {(lowercase+uppercase+otherSym+number,'q3')}}
    finalState = set(['q3'])
    i = 0
    state = 'q0'
    while (i < len(input)):
        found = False
        print(state)
        for trans in transisi[state]:
            for j in range(len(trans[0])):
                if (input[i] == trans[0][j]):
                    state = trans[1]
                    found = True
        if (found):
            i += 1
        else:
            break
    if (i == len(input) and state in finalState):
        return True
    else:
        return False



