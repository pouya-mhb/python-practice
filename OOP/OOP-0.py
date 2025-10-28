class ClassName:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        # Do some action
        return self.param1, self.param2


instance_of_object = ClassName("param 1", "param 2")
print(instance_of_object)
print(instance_of_object.some_method())

print(instance_of_object.param1)
print(instance_of_object.param2)


instance_of_class_2 = ClassName(1, 2)
print(instance_of_class_2.some_method())
