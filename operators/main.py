# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

spain_language = "Spanish"
switzerland_language = "German"
print(spain_language == switzerland_language)

spain_religion = "Roman Catholic"
switzerland_religion = "Roman Catholic"
print(spain_religion == switzerland_religion)

spain_capital = "Madrid"
switzerland_capital = "Bern"
print(len(spain_capital) != len(switzerland_capital))

spain_gpd = 1778000000000000
switzerland_gpd = 580000000000
print(switzerland_gpd > spain_gpd)

spain_pop_growth = 0.67
switzerland_pop_growth = 0.66
print(spain_pop_growth < 1 and switzerland_pop_growth < 1)

spain_pop = 50000000
switzerland_pop = 8400000
print(spain_pop > 10000000 or switzerland_pop > 10000000)

print(spain_pop > 10000000 and switzerland_pop <
      10000000 or spain_pop < 10000000 and switzerland_pop > 10000000)
