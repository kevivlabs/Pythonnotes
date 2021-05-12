def reverse_only_letters(text):
    """ leetcode 917"""
    s,i,j = list(text), 0, len(text)-1
    while i<j:
        if ( s[i].isalpha()) and (s[j].isalpha() ):
            s[i],s[j]= s[j],s[i]
            i +=1
            j -=1
        elif not (s[i].isalpha()):
            i +=1
        elif not (s[j].isalpha()):
            j -=1
    #print (type (str(s)))
    return print("".join(s))

reverse_only_letters("H3ll0 W0r$")
