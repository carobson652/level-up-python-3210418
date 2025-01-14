import random, time

def waiting_game():
  print ("Playing the waiting game.  Press enter to begin.", end="")
  input1 = input()
  waitTime = random.random() * 2.0 + 2.0
  print (f"Wait time is {waitTime:.3f} seconds. :", end = "")
  startTime = time.time()
  input1 = input()
  endTime = time.time()
  elapsed = endTime - startTime
  if elapsed < waitTime:
    print (f"Your wait time was {elapsed:.3f} seconds was too fast")
  elif elapsed > waitTime:
    print (f"Your wait time was {elapsed:.3f} seconds was too slow")
  else:
    print (f"Your wait time was {elapsed:.3f} seconds was perfect")

waiting_game()