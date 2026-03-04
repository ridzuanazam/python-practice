# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start(inclusive) : end(exclusive) : step(gap)]

credit_number = "1324-5678-9854-1254"

print(credit_number[1])
print(credit_number[0:7])
print(credit_number[:6])
print(credit_number[::3])
print(credit_number[::-1]) # reverse
print(f"XXXX-XXXX-XXXX-{credit_number[-4:]}")
