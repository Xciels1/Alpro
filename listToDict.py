def lstoDict(a, b):
    newdict = dict(zip(a,b))
    return newdict

a = ['red', 'green', 'blue']
b = ['#FF0000', '#008000', '#0000FF']

print(lstoDict(a, b))
