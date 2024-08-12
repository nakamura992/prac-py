def print_log(func):
    def wrapper(*args, **kwargs):
        print("\n####################")
        print("Start")
        print("####################")
        result = func(*args, **kwargs)
        return result
    return wrapper


@print_log
def say_greeting(name, greeting="Hello"):
    return f"{greeting} {name}"

@print_log
def print_text(text):
    return text

r = say_greeting("taro", greeting="Good Morning")
print(r)

s = print_text("test")
print(s)

"""
@print_logは
r = say_greeting("taro", greeting="Good Morning")
r("test", greeting="Good Morning")のような感じで
"""