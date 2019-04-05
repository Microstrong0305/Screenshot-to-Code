import os
import sys

import Levenshtein

argv = sys.argv[1:]

if len(argv) < 2:
    print("Error:not enough arguement supplied")
    exit(0)
else:
    path_pred = argv[0]
    path_fact = argv[1]
    
list = os.listdir(path_pred) #列出文件夹下所有的目录与文件
lratio = []
for i in range(0,len(list)):
    path1 = os.path.join(path_pred,list[i])
    path2 = os.path.join(path_fact,list[i])

    if os.path.isfile(path1):
        with open(path1,'r') as pre:
            temp1 = pre.read()
        with open(path2,'r') as fact:
            temp2 = fact.read()
        lenth1 = len(temp1)
        lenth2 = len(temp2)
        if lenth1 == lenth2:
            sim = Levenshtein.hamming(temp1, temp2)
            ratio = sim/lenth1
        else:
            ratio = 0
        lratio.append(ratio)
print("The error ratio on our corpus is about {}".format(sum(lratio) / len(lratio)))