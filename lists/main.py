# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line


def alphabetical_order(songs):
    return sorted(songs)


def won_golden_globe(film):
    awards = [
        'jaws',
        'star wars episode iv - a new hope',
        'e.t. the extra-terrestrial',
        'memoirs of a geisha']
    if film.lower() in awards:
        return True
    else:
        return False


def remove_toto_albums(list):
    toto_albums = [
        'Fahrenheit',
        'The Seventh One',
        'Toto XX(two previously unreleased songs)',
        'Falling in Between(sharing lead vocals on one song)',
        '35th Anniversary – Live in Poland',
        'Toto XIV',
        'Old Is New',
        '40 Tours Around the Sun',
        'With a Little Help from My Friends',
    ]
    new_list = list.copy()
    for word in list:
        if word in toto_albums:
            new_list.remove(word)
    return new_list
