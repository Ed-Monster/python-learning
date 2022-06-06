STARS = '******************************************************'

# create a list and print it
print('create a list and print it')
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print(STARS)

# get the last element
print('get the last element')
print(f'My latest auto is {motorcycles[-1]}.')
print(STARS)

# add a new element to its end
print('add "ford" to its end')
motorcycles.append('ford')
print(motorcycles)
print(STARS)

# pop an element
print('pop the last element')
last_ele = motorcycles.pop()
print(motorcycles)
print(f'My latest auto is {last_ele}.')
print(STARS)

# insert a new element
print('insert "ford" before the 2nd element')
motorcycles.insert(1, 'ford')
print(motorcycles)
print(STARS)

# remove an element by value
print('remove "ford"')
motorcycles.remove('ford')
print(motorcycles)
print(STARS)

# get the list size
print('The list has ', len(motorcycles), ' elements.')
print(STARS)

# sort the list
print('The list sorted temporarily:')
print(sorted(motorcycles))
print('The list reversely sorted permanently:')
motorcycles.sort(reverse=True)
print(motorcycles)