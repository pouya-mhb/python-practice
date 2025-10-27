a = [1, 2, 3, 4]
print(f"a is : {a}")

# def power_a(x):
#     return x**2

# for i in range(len(a)):
#     a[i] = power_a(a[i])

# print(f"power a is : {a}")

# now write it in lambda

power_a = map(lambda x: x**2, a)

print(power_a)

for i in power_a:
    print(i)

# ===========================

b = [5, 6, 2.1, 4.2, 1, 4.4, 6.5, 1, 3.2]


def is_float(x):
    return x != int(x)


print(list(filter(is_float, b)))

# now write it in lambda function
print(list(filter(lambda X: X != int(X), b)))

# ======================================
