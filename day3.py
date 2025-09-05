# For Loop
for i in range(1,6):
    print(i)


fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print(f)


# While Loop
i = 1
while i <= 5:
    print(i)
    i= i+1

# Nested Loops

for i in range(1,3):
    for j in range(1,3):
        print(i,j)

# Break & Continue
for i in range(1,6):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)

# Print all even numbers from 1–20

for i in range(1,21):
    if i % 2 == 0:
        print(i)
