def cakes(recipe, available):
    # TODO: insert code
    t=[]
    for i in recipe:
        if i in available:
            t.append(available[i] // recipe[i])
            return (min(t))
        else:
            return 0
          
'''
recipe ={'cream': 200, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
available = {'sugar': 1700, 'flour': 20000, 'milk': 20000, 'oil': 30000, 'cream': 5000}
cakes(recipe, available)
Fails : Need to check the code
'''
