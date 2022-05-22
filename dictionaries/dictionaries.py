
import pprint

a = {}
b = {'foo': 42, 'arno': 52}

print(a)
print(b['foo'])
print(b['arno'])

spam = {'bar': 100, 'cat': 123}
print('cat' in spam)
print('cat' in spam.keys())
print('cat' in spam.values())


if 'color' not in spam:
    spam['color'] = 'black'

spam.setdefault('arno', 'bla')


print(spam['arno'])


pprint.pprint(spam)
print(spam)