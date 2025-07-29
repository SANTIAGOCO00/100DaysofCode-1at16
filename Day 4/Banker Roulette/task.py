# Elegir un elemento al azar en una lista

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))

# Otra opción ...
friend_to_pay = random.randint(0, 4)
print(friends[friend_to_pay])