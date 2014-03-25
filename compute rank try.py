# Two Gold Stars
# Question 2: Combatting Link Spam

# One of the problems with our page ranking system is pages can 
# collude with each other to improve their page ranks.  We consider 
# A->B a reciprocal link if there is a link path from B to A of length 
# equal to or below the collusion level, k.  The length of a link path 
# is the number of links which are taken to travel from one page to the 
# other.

# If k = 0, then a link from A to A is a reciprocal link for node A, 
# since no links needs to be taken to get from A to A.

# If k=1, B->A would count as a reciprocal link  if there is a link 
# A->B, which includes one link and so is of length 1. (it requires 
# two parties, A and B, to collude to increase each others page rank).

# If k=2, B->A would count as a reciprocal link for node A if there is
# a path A->C->B, for some page C, (link path of length 2),
# or a direct link A-> B (link path of length 1).

# Modify the compute_ranks code to 
#   - take an extra input k, which is a non-negative integer, and 
#   - exclude reciprocal links of length up to and including k from 
#     helping the page rank.
def reciprocal_depth(graph,k):
    qlist=[]
    klist=[]
    for page in graph:
      ##
      for node in graph[page]:
        ##
        qlist.append([page,node])
    #print qlist
    if k==0:
      for link in qlist:
        if link[0] == link[1]:
          klist.append(link)
    if k==1:
      for link in qlist:
        if [link[1],link[0]] in qlist:
          klist.append(link)
    if k==2:
      t=0
      while t<len(qlist):
        tt=0
        while tt<len(qlist):
            if qlist[t][0]==qlist[tt][1]:
              if [qlist[tt][0],qlist[tt][1]] not in klist:
                klist.append([qlist[tt][0],qlist[tt][1]])
            tt=tt+1
        t=t+1
        
        t=0
        while t<len(qlist):
          tt=0
          while tt<len(qlist):
              if qlist[t][0]==qlist[tt][1]:
                if [qlist[tt][0],qlist[tt][1]] not in klist:
                  klist.append([qlist[tt][0],qlist[tt][1]])
              tt=tt+1
          t=t+1        
    print klist      
    for eachlink in klist:
      if [eachlink[1],eachlink[0]] not in klist:
        klist.append([eachlink[1],eachlink[0]])
            
    return klist 
    #print qlist
    #print klist
        
      
        
def reciprocal_depth_OOOL(graph,h):      
        list = []
        startdepth=[]
        enddepth=[]
        for k, v in graph.iteritems():
          #if v > 6:
            list.append([k,v])
        #print list
        #print list[0][0]# key
        #print list[0][1][0]# values
        i=0
        while i<h+1:
          #print list[0][0],list[0][1][i]
          startdepth.append([list[0][0],list[0][1][i]])
          #print str(h) + " h "
          i=i+1
          
        #print startdepth
          
          
          
          
        
        
        
        

      


def compute_ranks(graph,k):
    tracking=[]
    addedtrack=[]

    d = 0.8 # damping factor
    numloops = 10
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / (npages)
            for node in graph:
              
              
              #for each in reciprocal_depth(graph,k):
              #  if page==each[0] and node==each[1]:
              #       newrank = newrank - d * (ranks[node]/(len(graph[node])+0))
              


                # a->a, a->b, b->a, a->c, c->d, d->a links are reciprocal

                       
                #if page=="a" and node=="":
                #    newrank = newrank - d * (ranks[node]/(len(graph[node])+0))
                #if page=="a" and node=="":
                #    newrank = newrank - d * (ranks[node]/(len(graph[node])+0))                    
                #if page=="b" and node=="":
                #    newrank = newrank - d * (ranks[node]/(len(graph[node])+0))
                #if page=="a" and node=="":
                #    newrank = newrank - d * (ranks[node]/(len(graph[node])+0))
                #if page=="c" and node=="":
                #    newrank = newrank - d * (ranks[node]/(len(graph[node])+0))                    
                #if page=="d" and node=="n":
                #    newrank = newrank - d * (ranks[node]/(len(graph[node])+0))              
                    
                #print [page,node]  
                if [page,node] in reciprocal_depth(graph,k):
                    
                    #print [page,node]
                    #newrank = newrank
                    if [page,node] not in tracking:
                      tracking.append([page,node])
                    
                #elif k==2:
                #  newrank = newrank
                elif page in graph[node]: 
                  #if [page,node] is kk==False:
                  newrank = newrank + d * (ranks[node]/(len(graph[node])+0))
                  if [page,node] not in addedtrack:
                    addedtrack.append([page,node])
                    
                  #print page,node,newrank
  
            newranks[page] = newrank
        ranks = newranks
    print addedtrack, " what was added to the rank"
    print reciprocal_depth(graph,k), "what to exclude"
    print tracking, "tracking"    
    return ranks


# For example

g = {'a': ['a', 'b', 'c'], 'b':['a'], 'c':['d'], 'd':['a']}

#print reciprocal_depth(g,2)
#print compute_ranks(g,0) # the a->a link is reciprocal
#>>> {'a': 0.26676872354238684, 'c': 0.1216391112164609,
#     'b': 0.1216391112164609, 'd': 0.1476647842238683}

#print compute_ranks(g, 1) # a->a, a->b, b->a links are reciprocal
#>>> {'a': 0.14761759762962962, 'c': 0.08936469270123457,
#     'b': 0.04999999999999999, 'd': 0.12202199703703702}
#print g
#print reciprocal_depth(g,2)
#print compute_ranks(g, 2)
# a->a, a->b, b->a, a->c, c->d, d->a links are reciprocal
# (so all pages end up with the same rank)
#>>> {'a': 0.04999999999999999, 'c': 0.04999999999999999,
#     'b': 0.04999999999999999, 'd': 0.04999999999999999}

gg={'a': ['a', 'b', 'c'], 'c': ['d'], 'b': ['a'], 'e': ['b'], 'd': ['a', 'e']}

print compute_ranks(gg, 2)

