print(3 + 4)   # addition(+)
print(3 - 4)   # subtraction(-)
print(3 * 4)   # multiplication(*)
print(3 % 4)   # modulus(%)
print(3 / 4)   # division(/)
print(3 ** 4)  # exponential(**)
print(3 // 4)  # floor division operator(//)

print("")
print("30 days of python")
print("")

print(type(10))                         # Int
print(type(3.1))                        # Float
print(type(4 - 4j))                     # Complex
print(type('Matthew'))                  # String
print(type(True))                       # Boolean
print(type([10, 3.1, 'A', True]))       # List
print(type((10, 3.1, 'A', True)))       # Tuple
print(type({10, 3.1, 'A', True}))       # Set
print(type({'name':'Matt'}))            # Dictionary
print(type(None))                       # NoneType

def euclidean_distance(p1, p2, q1, q2):
    return ((q1 - p1)**2 + (q2 - p2)**2)**0.5

print(euclidean_distance(1,2,3,4))
print(euclidean_distance(9,8,7,6))
print(euclidean_distance(5,1,8,4))
print(euclidean_distance(10,11,0,0))
