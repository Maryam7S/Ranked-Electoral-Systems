from numpy import *

#DEFINE function to convert all votes into a single matrix

def reduce_votes(votes, N_candidates):

    pairwise_ballot=zeros([N_candidates, N_candidates]) #rows represent runners, columns represent opponents
    for ballot in votes:
        for a in range(N_candidates):
            for b in range(N_candidates):
                if a != b:
                    if ballot[a]>ballot[b]:
                        pairwise_ballot[a,b] +=1
    return(pairwise_ballot, N_candidates) 
