from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = 'c545bc87620d4ced81cbddb8a90b4a51'
__human_name__ = 'for'


""" Write your functions here. """


def shortest_names(countries):
    shortest_nr = 999
    shortest_list = []
    for country in countries:
        if len(country) < shortest_nr:
            shortest_nr = len(country)
    for country in countries:
        if len(country) == shortest_nr:
            shortest_list.append(country)
    return shortest_list


def get_nr_vowels(countries):
    vowels = 'aeiou'
    most_vowels = 0
    for country in countries:
        vowel_count = 0
        for letter in country:
            if letter.lower() in vowels:
                vowel_count += 1
        if vowel_count > most_vowels:
            most_vowels = vowel_count
    return most_vowels


def find_vowel_word(countries, number):
    vowels = 'aeiou'
    country_list = []
    for country in countries:
        vowel_count = 0
        for letter in country:
            if letter.lower() in vowels:
                vowel_count += 1
        if vowel_count == number:
            country_list.append(country)
    return country_list


def most_vowels(countries):
    most_list = []
    most_nr_vowels = get_nr_vowels(countries)
    for i in range(most_nr_vowels):
        most_list += find_vowel_word(countries, (most_nr_vowels - i))
    return most_list[:3]


def alphabet_set(countries):
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    alphabet_list = []
    for country in countries:
        for letter in country.lower():
            if letter in alphabet:
                alphabet_list.append(country)
                alphabet.remove(letter)
    return set(alphabet_list)


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == '__main__':
    countries = get_countries()

    """ Write the calls to your functions here. """
    shortest_names(countries)

    most_vowels(countries)

    alphabet_set(countries)
