#!/usr/bin/env python
# coding: utf-8

# In[68]:


'''An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
'''

import string
def is_isogram(s):
    t=s.lower()
    for i in t:
        if t.count(i) > 1:
            return False
    return True


is_isogram("moOse")


# In[ ]:





# In[ ]:





# In[ ]:




