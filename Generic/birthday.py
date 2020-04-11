# dictionary

birthdays = {'ajay raj': 'June 1', 'jaya prakash': 'Jan 22', 'prasanth kumar': 'Apr 04'}
print(list(birthdays))  # print the keys of dict
'''dict.keys() & dict.values() returns a tuple(immutable)'''
while True:
    name = input('Enter your friend name for birthday details (blank to quit)')
    if name =='':
        break
    if name in birthdays.keys():
        print(birthdays[name.lower()] + ' is the birthday of ' + name)
    else:
        print('Name is\'nt found in the database,please enter the birth date')
        birthdays[name.lower()] = input()
        print('updated database')
        for key, value in birthdays.items():
            print(key +' : '+value)

'''
get(key,val) - returns the val in case of absence of key, instead of key error
setdefault(key,val) - sets a default value to a key, if key is'nt present in the dict
pprint.pprint()- helps to print dictionary in a pretty manner
del dict[key] - removes that specific key-value pair form the dictionary
'''



