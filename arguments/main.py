# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Part 1: Greet Template

def greet(name, template= "Hello, <name>!"):
    hello_template = template.replace("<name>", name)
    return hello_template


# print(greet("Linda"))

# Part 2: Force

def force(mass, body= "earth"):
    lower = body.lower()
    surface_gravity = {
        "sun": 274,
        "jupiter": 24.9,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6, 
    }

    force = mass * surface_gravity[lower]
    return force


# print(force(0.1, "Sun"))
# print(force(0.1, "Earth"))
# print(force(0.1, "Pluto"))
# print(force(0.1))

# Part 3: Gravity

def pull(m1, m2, d):
    n = 0.00000000006674
    pull = n * ((m1 * m2) / (d**2))
    return pull


# print(pull(800, 1500, 3))