w1=['P']
w2=['E']
w3="QWEIPFGJKZXV"
w4="QWEIPFGJKZXV"
w5="QWEIPFGJKZXV"
w=''
i=0
for i in range(len(w1)):
    w=w1[i]
    for j in range(len(w2)):
        if w2[j] in w:
            continue
        w+=w2[j]
        for k in range(len(w3)):
            if w3[k] in w:
                continue
            w+=w3[k]
            for l in range(len(w4)):
                if w4[l] in w:
                    continue
                w+=w4[l]
                for m in range(len(w5)):
                    if w5[m] in w:
                        continue
                    w+=w5[m]
                    print(w,end="\t")
                    i+=1
                    if i==7:
                        print()
                        i=0
                    w=w[:4]
                w=w[:3]
            w=w[:2]
        w=w[:1]

    
