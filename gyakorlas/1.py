#  készíts programot ami egy bevitt mondatban megszámolja a számokat és a betűket (külön)
#  és kiírja az eredményt. pl: szia 123     -> betűk: 4, számok: 3

sentence = input('irj be egy mondatot: ')
# print(type(sentence))
digits = 0
letters = 0
for char in sentence:
  if char.isdigit():
    digits += 1
  if char.isalpha():
    letters += 1

print(f"betűk: {letters} számok: {digits}")

print(sentence)