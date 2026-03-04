# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = alloccate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align 
# :+ = use plus sign to indicate positive value
# := = place sign to leftmost positive
# :  = insert a space before positive numbers
# :, = comma seperator

price1 = 3.14159
price2 = -987.65
price3 = 12.34

# ROUND UP
print(f"Price 1 is RM{price1:.3f}")
print(f"Price 2 is RM{price2:.2f}")
print(f"Price 3 is RM{price3:.1f}\n")

# TOTAL SPACES GIVEN
print(f"Price 1 is RM{price1:10}")
print(f"Price 2 is RM{price2:10}")
print(f"Price 3 is RM{price3:20}")
print(f"Price 3 is RM{price3:015}\n")

# TOTAL jUSTIFY
print(f"Price 1 is RM{price1:<10}")
print(f"Price 2 is RM{price2:>10}")
print(f"Price 3 is RM{price3:^15}")
print(f"Price 3 is RM{price3:^015}\n")

# SIGN
print(f"Price 1 is RM{price1:+}")
print(f"Price 2 is RM{price2:+}")
print(f"Price 3 is RM{price3:+}")
print(f"Price 3 is RM{price3: }")
print(f"Price 1 is RM{price1*2000:,}\n")

# COMBINE ALL
print(f"Price 1 is RM{price1*2000:+,.2f}")