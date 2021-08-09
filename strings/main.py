# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_1 = "Ruud Gullit"
scorer_2 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = scorer_1 + ' ' + str(goal_0) + ', ' + scorer_2 + ' ' + str(goal_1)

report = scorer_1 + " scored in the " + str(goal_0) + "nd minute\n" + \
    scorer_2 + " scored in the " + str(goal_1) + "th minute"

player = "Hennadiy Lytovchenko"

first_name = player[0:player.find(" ")]

last_name_len = len(player[player.find(" "):-1])

name_short = player[0] + '.' + player[player.find(" "):20]

chant = (first_name + '! ') * (len(first_name) - 1) + first_name + '!'

if chant[-1] != ' ':
    good_chant = True
else:
    good_chant = False
