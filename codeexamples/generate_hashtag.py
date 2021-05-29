def generate_hashtag(s):
    
    if s=="":
        return False
    
    t= s.split()
    result=""
    for i in t:
        result += i.capitalize()
    if len(result)>140:
        return False
    else:
        return '#'+result
