import re

def count_words ( file ):
  wordDict = {}
  with open( file, "r") as file:
    words = re.findall(r"[0-9a-zA-Z-']+", file.read())
    for word in words:
        word = word.lower()
        if word in wordDict:
          wordDict[word] += 1
        else:
          wordDict[word] = 1
  
  count = 0
  for word in wordDict:
    count+= wordDict[word]
  print (f"Counted {count} words")

  counted = 0
  for word in sorted(wordDict, key=wordDict.get, reverse=True):
    print(f"{word:10s}   {wordDict[word]}")
    counted += 1
    if counted > 20:
      break

count_words ( "shakespeare.txt" )