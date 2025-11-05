def calc (a,b, oprand):
    def add(a,b):
        return a + b

    def mul (a,b):
        return a * b

    if oprand == 'add':
        return add(a,b)

    if oprand == 'mul':
        return mul(a,b)


result = calc (2,3,'mul')
print(result)