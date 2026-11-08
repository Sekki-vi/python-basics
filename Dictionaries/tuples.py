# Tuples are immutable sequences of objects.
# They can not be modified unlike lists

tuple1 = (1, 2, 3)
tuple2 = 1, 2, 3

print(tuple1)
print(tuple2)

# can be sliced or iterated over
for i in tuple1:
    print(i)

print(tuple1[0:2])

# can be concatenated
tuple3 = tuple1 + tuple2
print(tuple3)

# can be repeated
tuple4 = tuple1 * 3
print(tuple4)

# can not use functions that modify lists be they are immutable

tupleAnything = (1, 2, 3, "Hello", True, 4.5)
print(tupleAnything)

# can be nested
tupleNested = (1, 2, 3, (4, 5, 6))
print(tupleNested)

# can be unpacked
a, b, c, d = tupleNested
print(a)
print(b)
print(c)
print(d)