price = float(input('Please enter the price of the item: '))

tax = float(input('Please enter your local sales tax: '))

total = ((tax / 100) * price) + price


print('Your item\'s price is: $' + str(round(total, 2)))
