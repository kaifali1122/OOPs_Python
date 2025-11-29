from copy import copy , deepcopy

l1=[11,2,[3,4],5]

l2=copy(l1)
l3=deepcopy(l1)
l2[2].append(6)
l3[2].append(7)
print(l1)
print(l2)
print(l3)