class MyClass:
  pass


class Animal:
  exists = True

  # konstruktor, akkor fut le, amikor példányosítjuk az osztályt
  def __init__(self, age, max_age):
    self.age = age
    self.max_age = max_age
    self.alive = True
    print('Animal is created')

  def __str__(self):
    return f"This animal is {self.age} years old"

  def __repr__(self):
    return f"This animal is {self.age} years old"

  def eat(self):
    print('eating')

  def aging(self):
    self.age += 1
    if self.age >= self.max_age:
      self.alive = False


my_animal = Animal(10, 50)
my_animal2 = Animal(20, 100)

# Animal.exists = False
# print(my_animal.exists)
# print(my_animal2.exists)
# # print(my_animal.age)
# my_animal.eat()

# print(my_animal)


class Dog(Animal):
  def __init__(self, age, max_age, fur_length):
    super().__init__(age, max_age)
    self.fur_length = fur_length

  def barking(self):
    print('vau vau!')


my_dog = Dog(10, 15, 'long')
my_dog.barking()
my_dog.aging()
