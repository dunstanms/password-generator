import random
import string

length = 8

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = '.-_()#@!?~'

full = lower + upper + num + symbols

accounts = ['''Enter website to generate password''']

for i in range(1):
    tem = random.sample(full, length)
    password = ''.join(tem)
    print(f"{accounts}:{password}")