def a ():
    print ("hello world",)

b = a

a ()
b ()


def c():
    print ("hi")

def k(what_to_call):
    what_to_call()

k(c)
k(a)