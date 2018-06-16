print('小文字で入力してください．\nQuはqと入力してください．')
string = list(input())
string = "".join(sorted(string))

# 辞書をリストにする
with open("dictionary.txt", "r") as file:
    dictionary = list(map(str.strip, file.readlines()))

# 辞書のquをqに置換，インデックスを追加して，それぞれの文字列自体をソート
tmp_dictionary = []
for index, word in enumerate(dictionary):
    tmp = word.replace('qu', 'q')
    tmp = (''.join(sorted(tmp))).lower()
    tmp_dictionary.append([tmp, index])

# 全ての文字列をソート
sort_dictionary = sorted(tmp_dictionary, key = lambda x:x[0])

# 辞書にある単語の文字が入力した文字列に存在するかを確かめる関数
def is_in(sixteen, word):
    seen = -1
    for i in range(len(word)):
        flag = False
        for j in range(seen+1, 16):
            if word[i] == sixteen[j]:
                seen = j
                flag = True
                break
        if flag:
            continue
        else:
            return False
    return True

# 点数計算用の関数
def calculate_point(word):
    point = 0
    for i in range(len(word)):
        c = word[i]
        if  c=='j' or c=='k' or c=='q' or c=='x' or c=='z':
            point +=3
        elif c=='c' or c=='f' or c=='h' or c=='l' or c=='m'or c=='p' or c=='v' or c=='w' or c=='z':
            point += 2
        else:
            point +=1
    return point

max_point = 0
ans = ''

for i in range(len(sort_dictionary)):
    if is_in(string, sort_dictionary[i][0]):
        point = calculate_point(sort_dictionary[i][0])
        if point>max_point:
            max_point = point
            ans = dictionary[sort_dictionary[i][1]]

print(ans)