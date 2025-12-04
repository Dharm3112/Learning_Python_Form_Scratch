username = "Chai"

def func():
    username = "ChaiAurCode"

    print(username)

print(username)
func()

x = 99
# def func2(y):
#     z = x + y
#     return z
#
# print(func2(3))
#
# def func3():
#     global x
#     x = 12
# func3()
# print(x)

def f1():
    x = 88
    def f2():
        print(x)
    return f2
myresult = f1()
myresult()

def chai(num):
    def actual(x):
        return x ** num
    return actual

f = chai(2)
g = chai(3)

print(f(3))
print(g(3))