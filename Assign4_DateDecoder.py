
exampleStringToDecode = '8-MAR-85'

monthDict = {
    'JAN': '01',
    'FEB': '02',
    'MAR': '03',
    'APR': '04',
    'MAY': '05',
    'JUN': '06',
    'JUL': '07',
    'AUG': '08',
    'SEP': '09',
    'OCT': '10',
    'NOV': '11',
    'DEC': '12'

}

splitString = exampleStringToDecode.split('-')
print(splitString)

def YearMonthDay(val):
    splitVal = val.split('-')
    full_year = '19' + splitVal[2]
    month_as_numb = monthDict[splitVal[1]]

    newYeMoDa = (full_year, month_as_numb, splitVal[0])
    return newYeMoDa


print(YearMonthDay(exampleStringToDecode))
    