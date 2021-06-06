def anagrams(word,words):
    temp=[]
    myword=sorted(word)
    for i in words:
        if myword==sorted(i):
            temp.append(i)
    
    return temp
  
  anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
