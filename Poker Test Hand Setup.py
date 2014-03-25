import random
import string

#print ''.join(random.choice(string.ascii_uppercase) for _ in range(5))


def randomhand(nofcards=5):
  def ransuit():
    return ''.join(random.choice(['H','D','S','C']) for _ in range(1))

  finalhand=[]
  starthand= ''.join(random.choice(['A','2','3','4','5','6','7','8','9','T','J','Q','K']) for _ in range(nofcards))
  toadd=''
  for each in starthand:
    toadd=each+ransuit()
    if toadd in finalhand:
      rp=ransuit()
      while toadd[1] ==rp:
        rp=ransuit()
      toadd=each+rp
    finalhand.append(toadd)
  
  return " ".join(finalhand)
  
#hand= randomhand(5).split()
hand=['7S', 'AS', 'QH', 'TS', '7H']

def hand_rank(hand):
    ranks = [['--23456789TJQKA'.index(r),s] for r, s in hand]
    return ranks

print hand
print hand_rank(hand)

def h_highcard(hand):
  handlist=hand_rank(hand)
  return sorted(handlist, reverse=True)

print ""
print "high card"
print h_highcard(hand)

def h_findpairs(hand):
  compare=[]
  ranksorted=[rank for rank ,suit in h_highcard(hand)]
  pairs=[]
  for each in ranksorted:
    #print each
    if each not in compare :
      compare.append(each)
  pairs=[[ranks,0] for ranks in compare]
  for each in ranksorted:
    #print pair
    for pair in pairs:
      #print each,pair[0]
      #print each
      if each==pair[0]:
        
        pair[1]=pair[1]+1
      
  return pairs  
   
print "Pairs qts"
print h_findpairs(hand)  

# (1) Pair
# (2) Pairs
# 3okind
# straight
# flush
# full house or 3 of a kind with pair
# 4 of a kind
# straing flush

# full house

#straing flush



