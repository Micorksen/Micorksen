# Based from stacksmashing's video : Why 111-1111111 is a valid Windows 95 key.
# https://youtu.be/cwyH59nACzQ

from random import randint

# Generating the first part of the digits.
a = randint(100, 999)

while (a == 333 or a == 444 or a == 555 or a == 666 or a == 777 or a == 888 or a == 999):
  a = randint(100, 999)


# Generating the second part of the digits.
b = randint(1000000, 1111111)
valid = False

while not valid:
  i = 0
  digit_sum = 0
  checked = False

  while not checked:
    current = int([char for char in str(b)][i])
    if (current < 0 or current > 9):
      break

    digit_sum += current
    i += 1
    if (i > 6):
      checked = digit_sum % 7 == 0
      valid = checked
      break

  if not valid:
    b = randint(1000000, 1111111)
    i = 0
    digit_sum = 0


# Printing the result.
print(f'Your retail Windows 95\'s license key is: {a}-{b}')
print('Have a happy hacking time !')