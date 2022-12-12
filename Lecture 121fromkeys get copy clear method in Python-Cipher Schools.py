d = dict.fromkeys(['name','age','height'],'unknown')
print(d)

d = dict.fromkeys(['name','age'],['unknown','unknown'])
print(d)

d = {'name':'unknown','age':'unknown'}
print(d.get('names'))

if 'name' in d:
    print('present')
else:
    print('not present')

if d.get('name'):
    print('present')
else:
    print('not present')

d1 = d.copy()
print(d1)