class OOP:
    def __init__(self, state_var):
        self.state_var = state_var

    def method(self):
        return self.state_var


def func(state_var):
    state_like_var = state_var

    def method_like():
        return state_like_var

    def method_caller(method_name):
        if method_name == "method":
            return method_like()

    return method_caller


oop_version = OOP(0)
print(oop_version.method())

func_version = func(1)
print(func_version("method"))
