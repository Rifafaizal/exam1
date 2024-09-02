num=[10,10,20,20,20,21,22,23]

word_count={}
for w in num:
     if w in word_count:
        word_count[w]+=1
     else:
        word_count[w]=1
print(word_count)


word_count={}
for n in num:
    if n in word_count:
        word_count[n]+=1
    else:
        word_count[n]=1
print(set(word_count))