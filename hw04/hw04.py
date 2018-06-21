import numpy as np

wikilinks =  np.zeros(1483277)
indexs = []
with open('links.txt')as file:
    i = 0
    for line in file:
        wikilinks[int(line.strip().split("\t")[1])] += 1
        #デバッグ用
        # wikilinks = np.append(line.strip('\n'))
        # if i%10000000 == 0:
        #     print(i)
        # i += 1
    for index, v in enumerate(wikilinks):
        if v>=10000:
            # print(index)
            indexs.append(index)

with open('pages.txt') as file:
    titles = file.readlines()
for i in indexs:
    print(titles[i])