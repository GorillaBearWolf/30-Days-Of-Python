# Day 1: 30 Days of python programming

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

print(type(10))                         # int
print(type(3.1))                        # float
print(type(4 - 4j))                     # complex
print(type('A'))                        # string
print(type(True))                       # boolean
print(type([10, 'A', True]))            # list
print(type((10, 'A', True)))            # tuple
print(type({10, 'A', True}))            # set
print(type({'key1':'A', 'key2':10}))    # dictionary
print(type(None))                       # NoneType

def euclidean_distance(p1, p2, q1, q2):
    return ((q1 - p1)**2 + (q2 - p2)**2)**0.5

print(euclidean_distance(1,2,3,4))
print(euclidean_distance(9,8,7,6))
print(euclidean_distance(5,1,8,4))
print(euclidean_distance(10,11,0,0))
