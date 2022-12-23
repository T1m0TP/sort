# We import the numpy module
import numpy as np

print('''
          ((((( ☻ )))))
             __|_|_     _____
            /\/\/\/\   |   ♥ \  Github : T1m0TP
          <|\/\/\/\/|_/ /____/  Instagram : @codeur.tim
           |___________/         
           |_|_|  /_/_/
''')

# We define the array
toSort = np.random.randint(0, 100, 50)
# We create 2 loops
for i in range(len(toSort)):
    for j in range(len(toSort)):
        # We create a condition which gives the order of arrangement of the numbers
        if toSort[i] <= toSort[j]:
            # We classify the numbers
            toSort[i], toSort[j] = toSort[j], toSort[i]
print(toSort)
