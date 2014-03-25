def longest_repetition(lista):
  if lista==[]:
    return None
  if repetition(repetition(lista))==[]:
    return lista[0]

  if len(repetition(repetition(lista)))>2:
    return repetition(repetition(repetition(lista)))[0]
    
  return repetition(repetition(lista))[0]

def repetition(lista):

  

  e=0
  track=[]
  while e<len(lista):
    
    if lista[e]==lista[e-1]:
      track.append(lista[e-1])

    e=e+1
  #print track
  return track   
    



#For example,
print longest_repetition([2, 2, 2, 3, 3, 3, 3, 4, 4, 4])
#3

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

#print longest_repetition([])
# None
