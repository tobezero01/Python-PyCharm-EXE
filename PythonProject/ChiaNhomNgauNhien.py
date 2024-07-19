import random

def random_pair(groups):

  pairs = []
  while len(groups) >= 2:
    group_1 = random.choice(groups)
    groups.remove(group_1)
    group_2 = random.choice(groups)
    groups.remove(group_2)
    pairs.append((group_1, group_2))
  return pairs


groups = list(range(1, 15))
pairs = random_pair(groups)

for pair in pairs:
  print(pair)
