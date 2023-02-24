

Time of day
day
night

Cow milking status
Need milking: True
Don't need milking: False

Location of the cows
pasture
cowshed

Season
winter
spring
summer
fall

Slurry tank
Full: True
Not full: False

Grass status
Long: True
Short: False

# take cows to cowshed when:

# cows are on the pasture + night = true or,
# when cows are in the pasture + rainy = true or, 
#  milk cows (true when fertilize pasture)

# if slurry tank is full, 
# cows must be in cowshed
# the weather is not sunny or windy
# mow grass is true

# mow grass is true when:
# the grass is long
# It's spring
# the weather is sunny
# the cows are not on the pasture

# wait is when the is no other action. 

# Hello, (name

# (1) Python takes note of this function
def main():
    # (5) At this point greet() is known and we can run it.
    print(greet('Bob'))

# (2) Then this one
def greet(name):
    return f'Hi, {name}!'

# (3) Now this statement is read
if __name__ == '__main__':
    # (4) main is run
    main()