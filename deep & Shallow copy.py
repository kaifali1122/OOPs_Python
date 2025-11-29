# Shallow copy - duplicate object but only copy reference for
#                nested object, so change in nested object affect
#                both copies

# Deep Copy - create a fully independent copy include nested object 
#             so change in nested object does not affect both copies


# Need to import 
from copy import copy , deepcopy

l1=[11,2,[3,4],5]
print("Orignal list -                   ",l1) 

# Shallow copy 
l2=copy(l1)
l2[2].append(6)
print("Shallow copy  list -             ",l2)
print("Orignal list after shallow copy -",l1)

# Deep copy 
l3=deepcopy(l1)
l3[2].append(7)
print("Deep copy list -                 ",l3)
print("Deep copy list after deep copy  -",l1)
