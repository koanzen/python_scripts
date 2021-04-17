# tupples is like list but immutable or uneditable

coordinates = (1,2,3)

# unpacking assignments
# must have thesame numbers of variables and the item inside the tuple
# or you will get exceptions

x,y,z = coordinates

print(x)
print(y)
print(z)

# to ignore a index in a tuple

_, y, z = coordinates

print(y)
print(z)

_, _, z = coordinates

print(z)


# unpacking a tupple in a limited variable
# here we will use the asterix symbol to unpack remaining tuple values

x, y , *z = (1,2,3,4,5,6,7,8,9)

print(x)
print(y)
print(z)

x, y , *z, a, b, c = (1,2,3,4,5,6,7,8,9)

print(x)
print(y)
print(z)
print(a)
print(b)
print(c)

# to ignore the remaining items

x, y , *_, a, b, c = (1,2,3,4,5,6,7,8,9)

print(x)
print(y)
print(a)
print(b)
print(c)