def index_all(theList, item):
  retList = []
  if isinstance(item, list ):
    for subItem in item:
      matches = index_all(theList, subItem)
      for match in matches:
        retList.append(match)
  else:
    for i in range ( 0, len(theList) ):
      if isinstance(theList[i], list):
        for j in range (0, len(theList[i])):
          if isinstance(theList[i][j], list ):
            matches = index_all(theList[i][j], item)
            for match in matches:
              retList.append([ i, j, match ])
          else:
            if item == theList[i][j]:
              retList.append([i, j])
      else:
        if item == theList[i]:
          retList.append(i)
  return retList
       
example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
print ( str ( index_all ( example, 2) ))
print ( str ( index_all ( example, [ 1, 2, 3]) ))