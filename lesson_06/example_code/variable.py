# var1 是全局名称
var1 = 5
def some_func():
    var1 = 15
    print('var1:', var1)
    # var2 是局部名称
    var2 = 6
    print('var2:', var2)
    #print('var3:', var3)

    def some_inner_func(): 
        # var3 是内嵌的局部名称
        var3 = 7
        print('var1:', var1)
        print('var2:', var2)
        print('var3:', var3)


print(var1)
some_func()
# print('var2:', var2)
# print('var3:', var3)