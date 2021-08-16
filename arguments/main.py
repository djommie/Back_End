# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, template=f'Hello, <name>!'):
    greeting = template.replace('<name>', name)
    return greeting


def force(mass, body='earth'):
    planets = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6,
    }
    gravity = planets[body]
    force = mass * gravity
    return force


def pull(m1, m2, d):
    g = 6.674 * (10**-11)
    f = g * (m1 * m2) / d**2
    return f


print(pull(800, 1500, 3))
