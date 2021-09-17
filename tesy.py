x=0

def func():
    print("hello, i am in a function")
    global x
    x=1
    x=5

func()
x=10
print(x)
