import urllib.request
import requests
import urllib
from urllib.request import urlopen
import urllib3
import re
grey = "qwertyuiopasdfghjklzxcvbnm"
grey = re.sub("[ein]", "", grey)
yellow=""
w1="s"#grey+"ude"
w2="h"
w3=grey
w4=grey+""
w5=grey+""
w=''
cnt=0
flag=0
file_url = 'https://gist.githubusercontent.com/dracos/dd0668f281e685bad51479e5acaadb93/raw/6bfa15d263d6d5b63840a8e5b64e04b382fdb079/valid-wordle-words.txt'
words = urlopen(file_url).read().decode('utf-8')
words=words.split("\n")
for i in range(len(w1)):
    w=w1[i]
    for j in range(len(w2)):
        w+=w2[j]
        for k in range(len(w3)):
            w+=w3[k]
            for l in range(len(w4)):
                w+=w4[l]
                for m in range(len(w5)):
                    w+=w5[m]
                    if w.lower() in words:
                        for t in yellow:
                            if t not in w:
                                break
                        else:
                            print(w.upper(),end="\t")
                            cnt+=1
                            flag=1
                    if cnt==2:
                        print()
                        cnt=0
                        i=0
                    w=w[:4]
                w=w[:3]
            w=w[:2]
        w=w[:1]

if flag==0:
    print("no valid words from database")
