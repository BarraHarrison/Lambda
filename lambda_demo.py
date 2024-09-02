# Lambda function that returns 10, ignoring the input
# x = lambda a: 10

# print(x(5))  # This will print 10

def example_method(n):
    return lambda a: a * n  

doubler = example_method(2)
print("-------------------")
print(doubler(2))  
print(doubler(4))
print(doubler(8))
print("-------------------")

tripler = example_method(3)
print("-------------------")
print(tripler(3))
print(tripler(9))
print(tripler(12))
print("-------------------")

times_ten = example_method(10)
print("-------------------")
print(times_ten(3))
print(times_ten(9))
print(times_ten(12))
print("-------------------")