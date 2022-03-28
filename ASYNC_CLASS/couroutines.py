""" CORROTINAS - forma de escrever aplicações assincronas.
ENTENDENDO AS CORROTINAS"""

def coro():
    print("Started")
    
    while True:
        value = yield
        yield value + 10


c = coro()

print("------", next(c)) # printed value = None

print("------", c.send(10)) # printed value = 20

print("=-"*20)

def coro2():
    print("Started")
    
    while True:
        values = yield
        yield values

c_value = coro2()

print("------", coro2) # <function coro2 at 0x7f85130880d0>
print("------", next(c_value)) # None

print(c_value.send([1,2,3,4,5]))
print(next(c_value))