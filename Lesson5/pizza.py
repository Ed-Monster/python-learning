available_toppings = ['bacon', 'cheese', 'lettuce', 'ham', 'sashimi']

# requested_toppings = ['cheese', 'kushiyaki', 'ham']
requested_toppings = []                                 # a empty list

if requested_toppings:                                  # check if empty
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:     # check if in the list
            print(f'Adding {requested_topping}...')
        else:
            print(f'{requested_topping} is now not available!')
else:
    print('Are you sure you want a plain pizza?')