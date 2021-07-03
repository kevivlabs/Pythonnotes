from itertools import permutations as mypermutations

def permutations(string):
    
    t= set( mypermutations(string, len(string)))
    t2=[]
    for i in t:
        t2.append(''.join(i))
        #t2.append(temp)
    return t2
