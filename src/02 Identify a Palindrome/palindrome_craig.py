import re

def is_palidrome(phrase):
  forwards = "".join(re.findall('[a-z]', phrase.lower()))
  backwards = forwards[::-1]
  return ( forwards == backwards)
    

print(is_palidrome("Tacocat"))
print(is_palidrome("happyHappy"))
print(is_palidrome("racecar"))
print(is_palidrome("Go hang a salami, I'm a lasagna hog"))