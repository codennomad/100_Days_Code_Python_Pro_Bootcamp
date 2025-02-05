import random

friends = ["Alice", "Breandon", "Davi", "Gustavo", "Bjord"]

print(random.choice(friends))

random_index = random.randint(0, 4)
print(friends[random_index])