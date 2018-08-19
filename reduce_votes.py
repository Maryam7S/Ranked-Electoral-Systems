from numpy import *

#DEFINE function to convert all votes into a single matrix

def reduce_votes(votes, N_candidates):

    pairwise_ballot=zeros([N_candidates, N_candidates]) #rows represent runners, columns represent opponents
    for ballot in votes:
        for runner_index in range(N_candidates):
            for opponent_index in range(N_candidates):
                if runner_index != opponent_index:
                    if ballot[runner_index]>ballot[opponent_index]:
                        pairwise_ballot[runner_index,opponent_index] +=1
    return(pairwise_ballot, N_candidates) 
