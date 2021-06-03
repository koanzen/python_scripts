from typing import List
### Typing
## Support for type hints

## Indicating what type of variable
# common types you can use int, str, bool, float, bytes
var1: int = 1
var2: str = 'sample'

print(f'{var1} {var2}')

# In the function greeting, the argument name is expected to be of type str and the return type str.
# Subtypes are accepted as arguments.
def greeting(name: str) -> str:
    return 'Hello ' + name

print(greeting('World'))


## Type aliases
# A type alias is defined by assigning the type to the alias. In this example,
# Vector and [float] will be treated as interchangeable synonyms
Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# typechecks; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])

print(new_vector)