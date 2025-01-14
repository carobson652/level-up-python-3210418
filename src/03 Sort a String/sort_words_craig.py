import re

def sort_words ( string ) :
  words = re.split("\s+", string ) 
  print ("words   " + str(words) )
  sorted_list = " ".join( sorted(words, key = str.casefold ) )

  print ("String \"" + string + "\" sorted is \"" + sorted_list + "\"" )

sort_words("bananna ORANGE apple")