# mission : print > *********
#                    *******
#                     *****
#                      ***
#                       *
# 9,7,5,3,1 beza(-2)
# 0,1,2,3,4 beza(+1)
i = 0
j = 9
k = 5
"""
for x in range (i, k):
    print(" "*x, end="")
    print("*"*j)
    j -= 2
"""
#       OR

for x in range(i, k):
    print(" "*x + "*"* j)
    j -= 2

for x in range(1,10):
    print(x, end="  ")
print()

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(f"{symbol}", end="")
    print()