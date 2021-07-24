import random
import string


def password_generator():   
    lowercase = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
    uppercase = ''.join(random.choice(string.ascii_uppercase) for i in range(2))
    numeric = ''.join(random.choice(string.digits) for i in range(2))
    symbols = ''.join(random.choice(string.punctuation)for i in range(2))
    password = lowercase + uppercase + numeric + symbols
    return ''.join(random.sample(password, len(password)))
print(password_generator())