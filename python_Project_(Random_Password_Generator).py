"""
import random
import string

pass_len = 12

charValue = string.ascii_letters+string.punctuation+string.digits
password = ""

for i  in range(pass_len):
    password += random.choice(charValue)

print("Your Password is :",password)
"""

#            OR

import random
import string

pass_len = 4
charValue = string.digits+string.ascii_letters

password = "".join([random.choice(charValue) for i in range(pass_len)])

print("Your Password is :", password)