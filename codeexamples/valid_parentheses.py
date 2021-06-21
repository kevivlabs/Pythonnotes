def valid_parentheses(my_string):
    
    x=[]
    for i in my_string:
        #print(i)
        if i == "(":
            x.append(i)
        elif i == ")":
            try:
                x.pop()
            except:
                return False
        
    if len(x)==0: 
        return True
    else:
        return False


#Better Solution 

'''
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
    
''' 
