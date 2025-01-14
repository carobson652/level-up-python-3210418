import pickle

def save_dict( theDict, theFile ):
  with open ( theFile, "wb" ) as file:
    pickle.dump(theDict, file)

def read_dict( theFile ):
  with open ( theFile, "rb" ) as file:
    return pickle.load(file)


myDict = { "key1":"value1", "key2":"value2" }
save_dict ( myDict, "dictionary.dat" )

newDict = read_dict ( "dictionary.dat")
print ("Original dict = " + str(myDict))
print ("New dict      = " + str(newDict))
