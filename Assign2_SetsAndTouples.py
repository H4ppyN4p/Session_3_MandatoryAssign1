#print('its alive')

data = {'a': 'Alpha', 'b' : 'Beta', 'g': 'Gamma'}

listOfTuples = []
for val in data:
    print(val)
    keyValue = {val, data[val]}
    listOfTuples.append(tuple(keyValue))

print(listOfTuples)    