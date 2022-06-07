# loop through a list, using for loop
magicians = ['katie', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f'I can\'t wait to see your next trick, {magician.title()}.\n')


# using range(), starting from 1, stopping at 6
numbers = list(range(1, 6))
print('numbers = ', numbers, '\n')


# one argument, starting from 0 by default
numbers = list(range(6))
print('numbers = ', numbers, '\n')


# set the stride
even_numbers = list(range(2, 11, 2))
print('even_numbers = ', even_numbers, '\n')


# using a list comprehension to initialize a list
squares = [value**2 for value in range(1, 11)]
print('squares = ', squares, '\n')


# the syntax of slicing
players = ['judy', 'edward', 'akasaka', 'shirota', 'sakura']
print('players[1:3] = ', players[1:3])
print('players[:3] = ', players[:3])
print('players[3:] = ', players[3:])
print('players[-3:] = ', players[-3:], '\n')


# this code block shows the mechanism of python variables
my_food = ['sushi', 'tempuro', 'omuraisu', 'ramen']
friend_food = my_food[:]  # use slice to create a copy

my_food.append('torinabe')
friend_food.append('sembei')

print('my favorite food: ', my_food)
print('my friend\'s favorite food: ', friend_food, '\n')

my_food_err = ['sushi', 'tempuro', 'omuraisu', 'ramen']
friend_food_err = my_food  # friend_food_err and my_food_err point to the same memory block

my_food_err.append('torinabe')
friend_food_err.append('sembei')

print('my favorite food: ', my_food_err)  # the result is not expected
print('my friend\'s favorite food: ', friend_food_err, '\n')


# to use a tuple
# items of a tuple are unchangeable
dimensions = (200, 50)  # to define a tuple
for dimension in dimensions:
    print(dimension)
print('')

dimensions = (80,)  # redifine
for dimension in dimensions:
    print(dimension)
