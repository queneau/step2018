#数式を行で読み込み
def readNumber(line, index):
    number = 0
    flag = 0
    figure = 1
    while index < len(line) and (line[index].isdigit() or line[index] == '.'):
        if line[index] == '.':
            flag = 1
        else:
            number = number * 10 + int(line[index])
            if flag == 1:
                figure *= 0.1 
        index += 1
    token = {'type': 'NUMBER', 'number': number*figure}        
    return token, index


#各記号を認識
def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1


def readMul(line, index):
    token = {'type', 'MUL'}
    return token, index + 1


def readDiv(line, index):
    token = {'type', 'DIV'}
    return token, index + 1


def readLeftparen(left, index):
    token = {'type', 'LEFT'}
    return token, index + 1


def readRightparen(left, index):
    token = {'tyoe', 'RIGHT'}
    return token, index + 1


#記号をトークンに変換
def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMul(line, index)
        elif line[index] == '/':
            (token, index) = readDiv(line, index)
        elif line[index] == '(':
            (token, index) = readLeftparen(line, index)
        elif line[index] == ')':
            (token, index) = readRightparen(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens


def evaluate(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
        index += 1
    return answer


def test(line, expectedAnswer):
    tokens = tokenize(line)
    actualAnswer = evaluate(tokens)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expectedAnswer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
    print ("==== Test started! ====")
    test("1+2", 3)
    test("1.0+2.1-3", 0.1)
    print ("==== Test finished! ====\n")

runTest()

while True:
    print('> ',)
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)