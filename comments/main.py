# Do not modify these lines
__winc_id__ = '63ce21059cf34d3d8ffef497ede7e317'
__human_name__ = 'comments'

# Add your code after this line

"""This program wil calculate multiple costs of a vegan diet.
I have to write more stuff to make it multiple lines."""

# Prices per one vegetable
broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7

sum_one_each = sum([broccoli, leek, potato, brussel_sprout])

avg_price = sum_one_each / 4  # average price

# Number of vegetables we want to buy
num_potatoes = 7
num_broccolis = 5
num_leeks = 2
num_brussel_sprouts = 10

sum_total = (num_potatoes * potato) + (num_broccolis * broccoli) + \
    (num_leeks * leek) + (num_brussel_sprouts * brussel_sprout)

discount_percentage = 30  # 30% discount

discounted_sum_total = round(sum_total - ((sum_total/100) * 30), 2)

print(discounted_sum_total)

"""Here's a multiline comment.
It uses multiple lines and is the only comment type that we need to
terminate explicitly."""
