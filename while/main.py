from helpers import random_koala_fact

__winc_id__ = 'c0dc6e00dfac46aab88296601c32669f'
__human_name__ = 'while'


def unique_koala_facts(i):
    all_facts = [
        "Koalas are found in the eucalyptus forests of eastern Australia. They have grey fur with a cream-coloured chest, and strong, clawed feet, perfect for living in the branches of trees!",
        "The koala's nickname is a Native Bear.",
        "They live and sleep in the eucalyptus trees. It's hot, light and dry here.",
        "The koala breaths oxygen from air.",
        "Koalas live for 20 or more years.",
        "Cuddly critters, koalas measure about 60cm to 85cm long, and weigh about 14kg.",
        "The koalas have white on the underside and gray on the rest of its body.",
        "After 1 month the cub is 1 cm. long.",
        "Eucalyptus leaves are super tough and poisonous! Luckily for koalas, they have a long digestive organ called a cecum which allows them to break down the leaves unharmed.",
        "A joey grows and develops in the pouch for about six months. Once strong enough, the youngster rides around on its mother\u2019s back for a further six months, only using the pouch to feed.",
        "The koala cub stays in the mother's pouch for 5 months.",
        "Koala\u2019s grow up to become big eaters, shifting up to one kilogram of eucalyptus leaves in a day! They are fussy, too, and will select the most nutritious and tastiest leaves from the trees where they live.",
        "The koala might look cuddly but the koala has very sharp teeth and very sharp claws.",
        "One cub is born at a time.",
        "The koala weighs 15 to 30 pounds.",
        "Koalas are nocturnal marsupials famous for spending most of their lives asleep in trees. During the day they doze, tucked into forks or nooks in the trees, sleeping for up to 18 hours. This sedentary lifestyle can be attributed to the fact they have unusually small brains and survive on a diet of nutrient-poor leaves. Koalas tend to smell strongly of eucalyptus and musk. This is thought to discourage fleas and other animals from living in its fur",
        "Although you may have heard people call them koala \"bears\", these awesome animals aren't bears at all \u2013 they are in fact marsupials. A group of mammals, most marsupials have pouches where their newborns develop.",
        "The koala cub is blind when it's born.",
        "The mother has a pouch.",
        "The koala is a marsupial mammal.",
        "The koala's young is called a cub.",
        "Koalas sleep for up to 19 hours.",
        "The koala has big ears and a big nose.",
        "The koala has very thick fur.",
        "Koalas don\u2019t have much energy and, when not feasting on leaves, they spend their time dozing in the branches. Believe it or not, they can sleep for up to 18 hours a day!",
        "When an infant koala \u2013 called a joey \u2013 is born, it immediately climbs up to its mother\u2019s pouch. Blind and earless, a joey uses its strong sense of touch and smell, as well as natural instinct, to find its way.",
        "The koala's young are born alive.",
        "They are warm-blooded.",
        "These magnificent mammals get their name form an Aboriginal term meaning, \"no drink\". It\u2019s believed this is because koalas get almost all their moisture from the leaves they eat, and rarely drink water."]

    if i < len(all_facts):
        counter = 0
        fact_list = []
        while counter < i:
            new_fact = random_koala_fact()
            if new_fact not in fact_list:
                fact_list.append(new_fact)
                counter += 1
        return fact_list
    else:
        return all_facts


def num_joey_facts():
    fact = random_koala_fact()
    counter = 0
    number_of_joeys = 0
    counted_facts = []
    while counter < 10:
        new_fact = random_koala_fact()
        if 'joey' in new_fact and new_fact not in counted_facts:
            number_of_joeys += 1
            counted_facts.append(new_fact)
        if new_fact == fact:
            counter += 1
    return number_of_joeys


def koala_weight():
    weight = []
    while weight == []:
        fact = random_koala_fact()
        if 'kg' in fact:
            weight.append(fact[fact.find('kg')-2:fact.find('kg')])
    return int(weight[0])


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == '__main__':
    print(random_koala_fact())

    print(koala_weight())
