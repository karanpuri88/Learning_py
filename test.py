def test(n =1):
    print("This is inside function overwritten value", n)
n = 2
test(n)
print("This is outside function" , n)