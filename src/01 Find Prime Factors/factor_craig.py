def get_prime_factors(number):
  factors = []
  factor = 2
  while factor <= number:
    if number % factor == 0:
      factors.append(factor)
      number = number / factor
    else:
      factor += 1

  return factors


print (get_prime_factors(630))
print (get_prime_factors(13))
print (get_prime_factors(27))
print (get_prime_factors(27034532))
print (get_prime_factors(27034533432))
print (get_prime_factors(9927034533432))