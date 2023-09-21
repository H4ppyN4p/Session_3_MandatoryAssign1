#You should provide the solutions both using:
#   Set methods ( like: S1.union(S2) or S1.add(x)  ), and
#   Set oprators ( like: S1|S2 or S1&S2)

set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}


#Set Methods:
#Union Set Methods:
unionSetMethods = set1.union(set2)
print('Union Set Methods:')
print(unionSetMethods)
print('\n')

#Symmetric Difference Set Methods:
symDifferenceSetMethods = set1.symmetric_difference(set2)
print('Symmetric Difference Set Methods:')
print(symDifferenceSetMethods)
print('\n')

#Difference Set Methods:
differenceSetMethods = set1.difference(set2)
print('Difference Set Methods:')
print(differenceSetMethods)
print('\n')

#Disjoint Set Methods:
disjointSetMethods = set1.intersection(set2)
print('Disjoint Set Methods:')
print(disjointSetMethods)
print('\n')

#Set Operators:
#Union Set operators:
unionSetOperators = (set1 | set2)
print('Union Set Operators:')
print(unionSetOperators)
print('\n')

#Symmetric Difference Set Operators:
symmeetricDifferenceSetOperators = (set1 ^ set2)
print('Symmetric Difference Set Operators:')
print(symDifferenceSetMethods)
print('\n')

#Difference Set Operators:
differenceSetOperators = (set1 - set2)
print('Difference Set Operators:')
print(differenceSetOperators)
print('\n')

#Disjoint Set Operators:
disjointSetOperators = (set1 & set2)
print('Disjoint Set Operators:')
print(disjointSetOperators)
print('\n')