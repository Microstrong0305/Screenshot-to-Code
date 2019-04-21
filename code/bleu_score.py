import os
import sys
from nltk.translate.bleu_score import sentence_bleu

argv = sys.argv[1:]

if len(argv) < 2:
    print("Error:not enough arguement supplied")
    exit(0)
else:
    path_pred = argv[0]
    path_fact = argv[1]
    
list = os.listdir(path_pred) #列出文件夹下所有的目录与文件

bleu_score = []
for i in range(0,len(list)):
    path1 = os.path.join(path_pred,list[i])
    path2 = os.path.join(path_fact,list[i])
    if os.path.isfile(path1):
        with open(path1,'r') as pre:
            temp1 = pre.read()
        with open(path2,'r') as fact:
            temp2 = fact.read()
        score = sentence_bleu([temp2.split()], temp1.split())
        bleu_score.append(score)
print("The BLEU score on our corpus is about {}".format(sum(bleu_score) / len(bleu_score)))