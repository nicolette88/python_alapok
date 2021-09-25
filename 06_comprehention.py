x = [1, 2, 3, 4, 4]
out = []
for num in x:
  out.append(num**2)
print(out)

# list comprehention
out = [num**2 for num in x]
print(out)

# dict comprehention
users = [("bob", 12, "mechanic"), ("james", 43, "artist"),
         ("harry", 23, "teacher")]

users_mapping = {user[0]: user for user in users}

print(users_mapping)

print(users_mapping['james'])