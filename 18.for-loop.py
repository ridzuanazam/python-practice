# for loops = execute a block of code a fixed number of times.
#             You can iterate over to range, string, sequence, etc.

"""
for (counter)
range(inclusive, exclusive)
to reverse count : reversed(range(1,11))
to count by 2 use step : range(1, 11, 2)
to skip use : continue
to stop use : break

for x in range(1, 11):
    print(f"Hello World {x}")

for x in reversed(range(1, 11)):
    print(f"Hello World {x}")

for x in range(1, 11, 2):
    print(f"Hello World {x}")

for x in range(1,11):
    if x == 7:
        continue
    else:
        print(x)

for x in range(1,11):
    if x == 7:
        break
    else:
        print(x)

"""

for x in range(1,11):
    if x == 7:
        continue
    else:
        print(x)
