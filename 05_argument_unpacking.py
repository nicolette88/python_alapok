def named(**kwargs):
  print(kwargs)


named(name="bob", age=4, alive=True)

details = {"name": "bob", "age": 4, "alive": True}

named(**details)


def both(*args, **kwargs):
  print(args)
  print(kwargs)


nums = [2, 3, 4]

both(*nums, **details)