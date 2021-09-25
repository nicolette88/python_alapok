# lista típusok
my_list = [2, 3, 56, 6]

# a lista utolsó eleme
print(my_list[-1])

# tól:ig határ, az első inkluzív, a második exkluzív
print(my_list[1:3])

# ha nincs alsó vagy felső korlát:
print(my_list[:3])

print(my_list[2:])

my_nested_list = [[3, 4], [5, 6], [7, 8]]
# első lista első eleme:
print(my_nested_list[1][0])
# beteszi az 5-öst
my_list.append(5)

print(my_list)

print(4 in my_list)

if 6 in my_list:
  print('van benne 6-os')

# tuple típusok
my_tuple = (3, 'peter', 5)

# error
# my_tuple[0] = 4

# set: csak egyedi elemeket tartalmazhat, soha nem lesz benne kettő ugyanolyan elem
my_set = {2, 3, 4, 5}
print(type(my_set))

my_set = {3, 33, 3, 33, 3, 33}
print(my_set)

my_set.add(3)
print(my_set)

my_list = [3, 3, 3, 3, 4, 4, 4, 5, 5, 5]
unique = list(set(my_list))
print(unique)

my_dict = {"name": "Peter", "age": 4, "alive": True}

print(my_dict['name'])
print(my_dict.keys())
print(my_dict.values())

for index, key in enumerate(my_dict):
  print(key, my_dict[key])

if 'alive' in my_dict:
  print('benne van')
