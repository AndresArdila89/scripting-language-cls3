
L2 = [10, 20, 30, 40, 50]
print(L2)
L2[0] = 100
print(L2)

L2[1:3] = [200,300] ## update more than one element
print(L2)

L2[3:3] = [400,500]
print(L2)

L3 = [700,800, [800,900]]### nested list

print(L2 + L3)
print(L3*L2)

##L3 = []

del[L3] ##delete the list
## print(L3)

###======= Methods
L4 = ['Math', 'Algebra', 'Art']
L4.append('Comp Sci')
print(L4)
