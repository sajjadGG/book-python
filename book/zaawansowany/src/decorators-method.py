def method_decorator(fn):
    "Example of a method decorator"
    def decorator(*args, **kwargs):
        print("\tInside the decorator")
        return fn(*args, **kwargs)

    return decorator

class MyFirstClass(object):
    """
    This class has all its methods decorated
    """
    @method_decorator
    def first_method(self, *args, **kwargs):
        print("\t\tthis is a the MyFirstClass.first_method")

    @method_decorator
    def second_method(self, *args, **kwargs):
        print("\t\tthis is the MyFirstClass.second_method")

if __name__ == "__main__":
    print("::: With decorated methods :::")
    x = MyFirstClass()
    x.first_method()
    x.second_method()

"""
::: With decorated methods :::
	Inside the decorator
		this is a the MyFirstClass.first_method
	Inside the decorator
		this is the MyFirstClass.second_method
"""