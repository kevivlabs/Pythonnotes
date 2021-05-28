def move_zeros(array):
    
    temp=[]
    temp1=[]
    for i in array:
        if i ==0:
            temp.append(i)
        else:
            temp1.append(i)
    
    result=(temp1 +temp)
    
    return result

move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) # returns [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
