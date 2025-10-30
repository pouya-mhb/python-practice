
def divis(a,b):
    try:
        return a / b
    except Exception as e:
        print (f"The error is {e}")



print(divis(3,2))
print(divis(3,0))


print ('============================')

def divis2(a,b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print (f"b can not be 0")

    except Exception as e :
        print (f"Another Error Happend as {e}")
        return None


print(divis2('a',2))
print(divis2(3,0))


'''
try :
    # try this
except :
    # show exception
else :
    # will run if no exception happens
finally :
    # will be run in any case

'''
