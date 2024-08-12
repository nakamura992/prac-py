greeting_list = ['Hello', 'Hi', 'Hey', 'Good morning', 'Good afternoon', 'Good evening']

def greeting():
    for word in greeting_list:
        yield word

def counter(num = 10):
    for _ in range(num):
        yield 'run'

g = greeting()
c = counter()

print(next(g))
print(next(c))
print(next(g))