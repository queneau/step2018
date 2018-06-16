def readNumber(line, index):
    number = 0
    flag = 0
    keta = 1
    while index < len(line) and (line[index].isdigit() or line[index] == '.'):
        if line[index] == '.':
            flag = 1
        else:
            number = number * 10 + int(line[index])
            if flag == 1:
                keta *= 0.1
        index += 1
    token = {'type': 'NUMBER', 'number': number * keta}
    return token, index


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1


def readMul(line, index):
    token = {'type': 'MUL'}
    return token, index + 1


def readDiv(line, index):
    token = {'type': 'DIV'}
    return token, index + 1


def tokenize(line):
    tokens = []
    index = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    while index < len(line):
        if line[index].isdigit(): #数字かどうか
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMul(line, index)
        elif line[index] == '/':
            (token, index) = readDiv(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

def kakeruwarukesu(tokens):
    # print(tokens)
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'MUL':
            answer = tokens[index-1]['number'] * tokens[index+1]['number']
            break
        elif tokens[index]['type'] == 'DIV':
            answer = tokens[index-1]['number'] / tokens[index+1]['number']
            break
        else:
            index += 1
    if len(tokens) == index:
        return tokens
    else:
        tokens[index-1] = {'type': 'NUMBER', 'number': answer}
        del tokens[index]
        del tokens[index]   
        # print(tokens) 
        return tokens


def evaluate1(tokens): #単純計算
    # print(tokens) #デバッグ用
    answer = 0
    index = 1

    old = tokens
    while True:
        # print(tokens) #デバッグ用
        #コピーを渡す
        new = kakeruwarukesu(old[:])
        # これはそのものを渡してるから書き換わる
        # new = kakeruwarukesu(old)
        if new == old:
            break
        old = new
    tokens = new
    # print(tokens) #デバッグ用
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print ('Invalid syntax')
        index += 1
    return answer


def test(line, expectedAnswer):
    tokens = tokenize(line)
    actualAnswer = evaluate1(tokens)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print ("PASS! (%s = %f)" % (line, expectedAnswer))
    else:
        print ("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
    print ("==== Test started! ====")
    test("1+2", 3)
    test("1.0+2.1-3", 0.1)
    test("1+2*3", 7)
    test("1+6/3.0", 3.0)
    test("500/2+4*10-65", 225)
    test("10+2*5-30/2-38", -33)
    test("10/2*5/5*4+1", 21)
    print ("==== Test finished! ====\n")

runTest()

# while True:
#     print ('> ',)
#     line = input()
#     tokens = tokenize(line)
#     answer = evaluate(tokens)
#     print ("answer = %f\n" % answer)