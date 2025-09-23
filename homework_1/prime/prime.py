def is_prime(number:int):
  counter = 0
  for num in range(2, number + 1):
    is_prime = True
    for denominator in range(2, round(num**0.5) + 1):
      if num % denominator == 0:
        is_prime = False
        break
    if is_prime:
        counter += 1

  return counter

