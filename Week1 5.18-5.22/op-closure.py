

def adder(x):
    a = 3
    def wrapper(y):
        nonlocal a
        a *= a
        return x - y +a
    return wrapper

adder5 = adder(5)
print(adder5(10))
print(adder(5)(10))      #  等同于 adder5(10) 闭包的特点，闭包允许函数关联的参数与内部的参数关联，这正是它的特色
# 输出都是-5
print(adder.__closure__)
print(adder5.__closure__)
print(adder5.__closure__[0].cell_contents) # 所有函数均有 __closure__属性。若函数是闭包，它返回的是由 cell 对象 组成的元组对象。cell 对象的cell_contents 属性就是闭包中的自由变量。