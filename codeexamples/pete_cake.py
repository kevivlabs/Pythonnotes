def cakes(recipe, available):
    # TODO: insert code
    t=[]
    if len(recipe)<=len(available):
        for i in recipe:
            for j in available:
                if i not in available: 
                    return 0
                else:
                    if i==j:
                        
                        t.append(available[j] // recipe[i])
    else:
        return 0
    
    
    return (min(t))
                
                
            
     
'''        
recipe= {'cream': 200, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
availabe= {'sugar': 1700, 'flour': 20000, 'milk': 20000, 'oil': 30000, 'cream': 5000}       
#recipe = {'flour': 78, 'butter': 76, 'sugar': 35}
#available = {'crumbles': 8774, 'cocoa': 3484, 'oil': 664, 'eggs': 9322, 'butter': 6339, 'nuts': 8775, 'pears': 7239, 'apples': 1389, 'sugar': 1643, 'milk': 7924}
cakes(recipe,available)

better solution 
def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)
    '''
