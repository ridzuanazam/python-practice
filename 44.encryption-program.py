import random
import string

chars = " "+string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars : {chars}")
# print(f"key : {key}")

# ENCRYPTION
plain_text = input("Enter a message to encrypt: ")
chiper_text = ""

for letter in plain_text:
    index = chars.index(letter)
    chiper_text += key[index]

print(f"original message : {plain_text}")
print(f"encrypted message : {chiper_text}")

# DENCRYPTION
chiper_text = input("Enter a message to dencrypt: ")
plain_text = ""

for letter in chiper_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message : {chiper_text}")
print(f"chipper message : {plain_text}")
