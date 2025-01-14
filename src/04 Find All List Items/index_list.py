def index_all(theList, item):
  retList = []
  for index,value in enumerate(theList):
    if value == item:
      retList.append([index])
    else:
      if isinstance(value, list):
        for subIndex in index_all( value, item ):
          retList.append( [index] + subIndex )
  return retList
       
example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
print ( str ( index_all ( example, 2) ))
print ("")
print ( str ( index_all ( example, [ 1, 2, 3]) ))