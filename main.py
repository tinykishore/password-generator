import random
import array
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
    exit(-1)

if len(sys.argv) > 2:
    print("Too much arguments")
    exit(-1)

passwordLength = int(sys.argv[1])

# Characters for generating password:
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
CHAR_LOW = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']
CHAR_UP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
           'X', 'Y', 'Z']
SYM = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
COMBINE = DIGITS + CHAR_LOW + CHAR_UP + SYM

randomDigit = random.choice(DIGITS)
randomCDown = random.choice(CHAR_LOW)
randomCUp = random.choice(CHAR_UP)
randomSym = random.choice(SYM)

temporaryPassword = randomDigit + randomCDown + randomCUp + randomSym

for x in range(passwordLength - 4):
    temporaryPassword = temporaryPassword + random.choice(COMBINE)
    tpl = array.array('u', temporaryPassword)
    random.shuffle(tpl)

finalPassword = ""

for x in tpl:
    finalPassword = finalPassword + x

print(finalPassword)