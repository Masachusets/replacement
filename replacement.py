def replace(a, b):
    a = a + b
    b = a - b
    a = a - b
    print('a = ' + str(a) + ';')
    print('b = ' + str(b) + ';')

a = 4
b = 5

replace(a, b)