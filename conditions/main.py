# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


def farm_action(weather, time, milking_status, cow_location, season, slurry_tank, grass_status):
    if cow_location == 'pasture':
        if time == 'night' or weather == 'rainy':
            return'take cows to cowshed'
        elif milking_status == True:
            return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'
        elif slurry_tank == True and weather == 'sunny' or weather == 'windy':
            return'take cows to cowshed\nfertilize pasture\ntake cows back to pasture'
        elif grass_status == True and season == 'spring' and weather == 'sunny':
            return 'take cows to cowshed\nmow grass\ntake cows back to pasture'
    elif cow_location == 'cowshed':
        if milking_status == True:
            return 'milk cows'
        elif slurry_tank == True and weather != 'sunny' or slurry_tank == True and weather != 'windy':
            return 'fertilize pasture'
        elif grass_status == True and season == 'spring' and weather == 'sunny':
            return'mow grass'
        return 'wait'
    else:
        return 'invalid input, please try again'
