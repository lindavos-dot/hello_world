x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)

'I like ' + str(3.14)
print('I like ' + str(3.14))

example_one = "I\'m a string."
example_two = "I'm a string."
example_three = "He said: 'I\'m a string'"
print(example_one)
print(example_two)
print(example_three)

type('I am too.')
print(type)

print("This string contains a double quote (\") character.")

print('a\
... b\
... c')

print('foo\\bar')

print("a\tb")
print("a\141\x61")
print('\u2192 \N{rightwards arrow}')

print('foo\nbar')
print(r'foo\nbar')
print('foo\\bar')
print(R'foo\\bar')
print('''This string has a single (') and a double (") quote.''')
print("""This is a
string that spans
across several lines""")

print(ord('a'))

s = 'I am a string.'
print(len(s))

s = "foobar"

print(s[3])

n = 20
m = 25
prod = n * m
print(f'The product of {n} and {m} is {prod}')

s = "foobar"
s = s.replace("b", "x")
print(s)

print('foo bar foo baz foo qux'.rfind('foo'))
