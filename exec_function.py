# executing a program constructed in a string
# and using the process.

# executing a function string
x = 'def test(a):'\
    '   return a'

exec(x)

print(test('Testing'))