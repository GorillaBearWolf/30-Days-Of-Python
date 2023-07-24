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

def euclidean_distance(p, q):
    return ((q[0] - p[0])**2 + (q[1] - p[1])**2)**0.5

print(euclidean_distance([1,2],[3,4]))      # input as list
print(euclidean_distance((91,9),(7,71)))    # input as tuple
