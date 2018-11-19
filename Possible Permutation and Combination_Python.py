# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 07:24:16 2018

@author: sajid Ullah
"""
                                #PERMUTATION
 
from itertools import permutations 
  
# Get all permutations of length 2 
# and length 2 
perm = permutations([10, 20, 30, 40, 50], 3) 
  
# Print the obtained permutations 
for i in list(perm): 
    print ("Perm:",i)
                                #COMBINATIO#

#print all combinations of given length 
from itertools import combinations 
  
# Get all combinations of [1, 2, 3] 
# and length 2 
comb = combinations([10, 20, 30, 40, 50], 3) 
  
# Print the obtained combinations 
for i in list(comb): 
    print ("Comb:",i) 
