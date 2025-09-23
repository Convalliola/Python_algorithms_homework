def is_palindrom(number: int):
  original_number = number
  reversed_number = 0
  while number > 0:
    digit = number%10
    number = number//10
    reversed_number = reversed_number*10 + digit
  if original_number == reversed_number:
    return True
  return False
