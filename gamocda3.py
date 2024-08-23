def last_survivor(l, c): 
    for i in c:
        l=l[:i]+l[i+1:]
    return l 