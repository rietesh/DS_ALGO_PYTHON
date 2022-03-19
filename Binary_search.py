def bsearch(seq, v):
    mp = len(seq)//2
    if mp == 0:
        return False
    print(mp, seq)
    if seq[mp] == v:
        return True    
    elif v > seq[mp]:
        return bsearch(seq[mp:], v)
    else:
        return bsearch(seq[:mp],v)

s = []
print(bsearch(s, 11))
