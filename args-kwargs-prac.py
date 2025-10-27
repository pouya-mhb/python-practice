def zarb(*args):
    res = 1
    for i in args:
        res *= i
    return res


print(zarb(1, 2, 3, 4))


def show(**kwargs):
    print(kwargs)


show(name="pouya", age=30)

# ==============================================


def sum_nums(*args):
    result = 0
    for num in args:
        result += num
    return result


def sum_nums_2(*args):
    result = 0
    result = sum(args)
    return result


print(sum_nums())
print(sum_nums(5, 10, 15))

print(sum_nums_2())
print(sum_nums_2(7, 3, 2, 1, 9))

# ==============================================

even_nums = []


def pick_evens(*args):
    for num in args:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums


# print(pick_evens(1, 2, 3, 4, 5, 6))
print(pick_evens(7, 13, 19, 21))

# ==============================================
"""
بلندترین ساختمان در افق
شما باید یک تابع به نام skyline(*args) بنویسید که ارتفاع تعدادی ساختمان را دریافت کند و بلندترین ارتفاع را برگرداند.

وظیفه شما:
تابعی به نام skyline(*args) بنویسید که:تعدادی عدد صحیح (ارتفاع ساختمان‌ها) را به عنوان ورودی دریافت کند.
بیشترین عدد را از بین آن‌ها پیدا کند و برگرداند.
اگر هیچ عددی وارد نشد، مقدار 0 را برگرداند.

ورودی‌ها:
چندین عدد صحیح که نمایانگر ارتفاع ساختمان‌ها هستند.

خروجی‌ها:
یک عدد صحیح که بلندترین ساختمان را مشخص می‌کند.
اگر هیچ مقداری داده نشود، مقدار 0 را برگرداند.
"""


def skyline(*args):
    if not args:
        return 0
    return max(args)


print(skyline(1, 5, 3, 9, 2))
print(skyline(1, 1, 1, 1, 1, 1, 1))
print(skyline())
