def vowels_count(s):
    num = 0
    sample= ['a','e','i','o','u']
    for i in s:
        if i in sample:
            num+=1
        
    
    return num
vowels_count("hdsfieoua")
