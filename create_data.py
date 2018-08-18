from numpy import *
import random

#imagine that an organization is voting on a candidate to fill a vacancy on its board of directors
#the candidates' names are Bruno, Cardi, Rocky
candidate_order = ('Bruno', 'Cardi', 'Rocky') 
N_candidates = len(candidate_order)

#assign random votes
N_voters = 10 #number of voters
votes = zeros([N_voters, N_candidates])
ballot = zeros(N_candidates)   
for i in range(N_voters):
    for a in range (N_candidates):
        ballot[a]= random.randint(1, 5) 
    votes[i]=ballot

savetxt('cast votes.csv', votes, delimiter=' ', newline='\n')
#savetxt('candidate list.txt', candidate_order)
f= open('candidate list.txt', "w")
f.write(' '.join(candidate_order))
f.close()
