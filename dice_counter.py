import random

frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0

for roll in range(600):
    face = random.randrange(1,7)
    
    if face == 1:
        frequency1 += 1
    elif face == 2:
        frequency2 += 1
    elif face == 3:
        frequency3 += 1
    elif face == 4:
        frequency4 += 1
    elif face == 5:
        frequency5 += 1
    elif face == 6:
        frequency += 1

print(f"{frequency1}")
print(f"{frequency2}")
print(f"{frequency3}")
print(f"{frequency4}")
print(f"{frequency5}")
print(f"{frequency6}")

    
