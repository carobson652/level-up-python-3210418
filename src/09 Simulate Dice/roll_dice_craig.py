import random

def roll_dice( *args ):
  numRolls = 500000
  maxRoll  = 0
  for arg in args:
    maxRoll += int(arg)

  freq = [0 for i in range(0,(maxRoll+1))]
  for num in range(0,numRolls):
    sum = 0
    for arg in args:
      number = random.randint(1, ( arg ) )
      sum += number
    freq[sum] += 1

  myString = ' '.join(str(arg) for arg in args)


  print ("Value   Probability for " + myString )
  for i in range (len(args), ( maxRoll + 1 ) ):
    prob = freq[i] / numRolls * 100 
    print (f"{i}       {prob:.3f}%")
  print ("")


roll_dice ( 6 )
roll_dice ( 6, 6, 6 )