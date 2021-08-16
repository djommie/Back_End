# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

leek_price = 2
print('Leek is ' + str(leek_price) + ' euro per kilo.')

leek_order = 'leek 4'
leek_number = int(leek_order[leek_order.find('4')])
sum_total = leek_number * leek_price
print(sum_total)

broccoli_price = 2.34
broccoli_order = 'broccoli 1.6'
broccolo_kgs = float(broccoli_order[broccoli_order.find(
    '1'):broccoli_order.find('6')+1])
broccoli_total = round(broccolo_kgs * broccoli_price, 2)
print(str(broccolo_kgs) + 'kg broccoli costs ' + str(broccoli_total) + 'e')
