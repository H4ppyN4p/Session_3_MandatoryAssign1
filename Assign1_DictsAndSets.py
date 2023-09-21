#Using virutal environment; check requirements.txt for needed pip installs


BoardOfDirectors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
Management = {'Tine', 'Trunte', 'Rane'}
Employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

#print(Employees)

print('who in the board of directors is not an employee?')
print(BoardOfDirectors - Employees )
print('\n')

print('who in the board of directors is also an employee?')
print(BoardOfDirectors & Employees)
print('\n')

print('how many of the management is also member of the board?')
print(len(BoardOfDirectors & Employees))
print('\n')

print('Are all members of the managent also an employee?')
print(len(Management) == len(Management & Employees))
print('\n')

print('Are all members of the management also in the board?')
print(len(Management) == len(Management & BoardOfDirectors))
print('\n')

print('Who is an employee, member of the management, and a member of the board?')
print(BoardOfDirectors & Management & Employees)
print('\n')

print('Who of the employee is neither a memeber or the board or management?')
print(Employees - BoardOfDirectors - Management)

