import random

def generate_passphrase ( num_words, wordlist_path='diceware.wordlist.asc'):
  word_list = {}
  with open ( wordlist_path, "r" ) as file:
    lines = file.readlines()[2:7778]
    for line in lines:
      x = line.split()
      key = x[0]
      value = x[1]
      word_list[key] = value

    words = []
    for i in range ( 0, num_words):
      index = str(roll_die()*10000+roll_die()*1000+roll_die()*100+roll_die()*10+roll_die())
      words.append(word_list[index])

  string = " ".join(words)
  print ("Passphrase = " + string )

def roll_die ():
  return random.randint(1,6)

generate_passphrase( 5 )
generate_passphrase( 7 )