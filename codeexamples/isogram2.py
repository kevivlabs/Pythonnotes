def is_isogram(s):
    return  len(s) == len(set(s.lower()))
        
    
is_isogram("mose")
