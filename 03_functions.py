def my_funct():
  pass


def add_user(users, new_user):
  users.append(new_user)


users = []
add_user(users, 'John')
# new_users = users.copy()
new_users = users
new_users.append('Kate')
print(users)


# positional argument: az argumentum pozíciója alapján van beazonosítva, hogy hányadk helyen áll a definícióban
def set_name(name, new_name):
  name = new_name
  return name

  # pass by reference VS pass by value


name = 'John'
new_name = name
new_name = 'Kate'
name = set_name(name, 'Peter')
# nem módosítja a name változó értékét, mert a name változó érték szerint adódik át a set_name függvénynek
set_name(name, 'Kate')
print(name)

vechicle = 'bus'


def drive():
  global vechicle
  vechicle = vechicle.capitalize()
  print(f'driving a {vechicle}')


drive()


def times2(num):
  return num * 2


seq = [3, 4, 5, 5]

times2_seq = list(map(times2, seq))
print(times2_seq)

# lambda: névtelen függvén (u. azt jelenti, mint a 44-45. sor)
times2_seq = list(map(lambda num: num * 2, seq))
print(times2_seq)

# a seq változóban megkeressük azokat a számokat, amik oszthatók 2-vel
filtered_list = list(filter(lambda num: num % 2 == 0, seq))
print(filtered_list)

# error: mindig annyi bemeneti paraméterrel dolgozzunk, amennyit a fv vár (itt 1 db)
# times2(4)

# keyword argument: a fv paramétereit úgy is meg lehet adni, hogy a definícióban létrehozott változók neve alapján hivatkozunk az argumentumokra, ilyenkor a sorrend nem számít
set_name(new_name='Kate', name='Peter')


def multiply(*nums):
  print(nums)
  total = 1
  for num in nums:
    total = total * num
  return total


val = multiply(2, 3, 4, 5, 5)
print(val)
