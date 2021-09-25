# készíts egy függvényt ami megállapítja egy stringről ami zárójeleket tartalmaz {}, (), []
# a függvény állapítsa meg hogy az összes zárójelnek megvan-e a párja


def find_closing(c, string: str):
  return string.find(c) > 0


def valid_braces(string) -> bool:
  if string == '':
    return False
  if len(string) % 2 != 0:
    return False
  parentheses = {"{}", "[]", "()"}
  while len(string) != 0:
    previous_length = len(string)
    for p in parentheses:
      string = string.replace(p, '')
    if len(string) == previous_length:
      return False
  return True


print(valid_braces("([)]"))  # ❌
print(valid_braces("([([])})"))  # ❌
print(valid_braces("(){()(([]))}"))  # ✅