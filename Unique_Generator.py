from datetime import datetime
import random

def generate():
    year_prefix = str(datetime.now().year % 100)
    random7digits = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    random9digits = year_prefix + random7digits
    checksum = sum(int(digit) for digit in random9digits) % 10
    membership_id = int(random9digits + str(checksum))
    return membership_id

#print(generate())