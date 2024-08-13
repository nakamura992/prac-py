from package import utils

print(utils.add_num(1, 2))

print("hello")

# 一行が長くなる時

""" これはエラー
a = 'aaa'
    + 'bbb'
"""
a = 'aaa' \
    + 'bbb'
print(a)

x = 10
y = 20
z = 30
if x < 0:
    print('xは0より小さい')
elif x < 15:
    print('xは15より小さい')