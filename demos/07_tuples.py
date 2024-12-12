def test_tuple():
    return ("val1","val2","val3")

print(test_tuple())

var1,var2,var3 = test_tuple()
print(var1)
print(var2)
print(var3)

for _ in range(0 , 10):
    print("test")

# Pour ignorer la varible 2
var1, _, var3 = test_tuple