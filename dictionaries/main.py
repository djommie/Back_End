from helpers import get_countries

__winc_id__ = '25a8041d2d5e4e3ab61ab1be43bfb863'
__human_name__ = 'dictionaries'


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
        'name': name,
        'date_of_birth': date_of_birth,
        'place_of_birth': place_of_birth,
        'height': height,
        'nationality': nationality
    }
    return passport


def add_stamp(dict, country):
    if 'stamps' not in dict and country != dict['nationality']:
        dict.update({'stamps': [country]})
        return dict
    elif country == dict['nationality'] or country in dict["stamps"]:
        return dict
    else:
        dict["stamps"].append(country)
        return dict


# Code voor checken foutieve test Winc

# def check_passport(passport, country, allowed, not_allowed):
#     nationality = passport['nationality']
#     print(passport, country, allowed, not_allowed)
#     if country in not_allowed.keys():
#         for destination in passport['stamps']:
#             print(destination)
#             print(nationality)
#             print(not_allowed)
#     elif country in allowed[nationality]:
#         return add_stamp(passport, country)


def check_passport(passport, country, allowed, not_allowed):
    nationality = passport['nationality']
    if country in not_allowed.keys():
        if nationality in not_allowed[country]:
            return False
        for destination in passport['stamps']:
            if destination in not_allowed[country]:
                return False
    elif country in allowed[nationality]:
        return add_stamp(passport, country)
