kapcsolo = True

if kapcsolo == True:
  print('a kapcsolo fel van kapcsolva')

print('ez mindig lefut')

name = 'Peter'
age = 5

print(f'hello {name}, your age is {age}')

# python3.6 felett:
print('hello {} your age is {}'.format(name, age))

szam = 10
while szam > 0:
  print(f'a szambol levontunk egyet: {szam}')
  szam -= 1

my_list = [3, 4, 5, 5]

for num in my_list:
  print(num)

for i in range(5):
  print(i)

for index, item in enumerate(my_list):
  print(f'{index}: {item}')
