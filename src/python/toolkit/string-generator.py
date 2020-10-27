import random
import string

characters = string.ascii_lowercase + string.digits + "#$@%&*!\\+-_/="
stringLength = 16
generatedString = ''.join([random.choice(characters) for i in range(stringLength)])

print('generated string: ', generatedString)