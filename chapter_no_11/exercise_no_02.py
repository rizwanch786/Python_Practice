def func(l, **kwargs):
    if kwargs.get('reversed_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title for name in l]
names = ['muhammad', 'rizwan']
print(func(names, reversed_str = True)