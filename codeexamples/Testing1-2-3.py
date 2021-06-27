def number(lines):
    k=1
    out=[]
    if len(lines) == 0:
        return out
    for i in lines:
        out.append( (f"{k}: {i}") )
        k+=1
    return out
  
  #should use enumerate ( but didnt know we could specify enumerate start=1)
  
  
