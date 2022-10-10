print('Me' == 'Me')
print('You' == 'Me')
print('Me' == 'me')

print('Hello, ' + 'world!')
print('Jump! ' * 5)

print('Samuel' in 'We went out for dinner with with Anne, Samuel and Bob.')
print('Shane' in 'We went out for dinner with with Anne, Samuel and Bob.')
print(str(5) in 'We were lucky that they had a table for 5.')

letter_grades = 'ABCDF'
print(letter_grades)
print(letter_grades[0])
print(letter_grades[3])

letter_grades = 'ABCDF'
print(letter_grades)
print(letter_grades[-1])
print(letter_grades[-2])
print(letter_grades[-2] == letter_grades[3])

waltz = 'onetwothree'
print(waltz[:3]) # We don't need to specify the 0 if we start at the beginning
print(waltz[:3])
print(waltz[3:6])
print(waltz[6:11]) # Same goes for the end -- we can leave it empty
print(waltz[6:]) # We can specify a step size if we don't want a continuous slice
print(waltz[:11:2])

sentence = 'The length of this string is:'
print(sentence, len(sentence))
print('Wait.. You just made it longer!')

answer = 42
qa = f'The answer is.. {answer}'

s = 'foo'
t = 'bar'
u = 'baz'

print(s + t)

print(s + t + u)


print('Go team' + '!!!')

print(s *4)
print(4 * s)