#!/usr/bin/env python3
###########shebang line, tells shell what to do with file

#Kemeny-Young method of voting
#The kemeny-young method is a condorcet method of voting. It satisfies the criterias
#of unrestricted domain and pareto efficiency but fails independence of irrelevant alternatives

from numpy import *
import random
import itertools
#################################################
#DEFINE function to process ballots
def reduce_votes(votes, N_candidates):

    pairwise_ballot=zeros([N_candidates, N_candidates]) #rows represent runners, columns represent opponents
    for ballot in votes:
        for a in range(N_candidates):
            for b in range(N_candidates):
                if a != b:
                    if ballot[a]>ballot[b]:
                        pairwise_ballot[a,b] +=1
    return(pairwise_ballot, N_candidates) 

#################################################
#DEFINE function to determine Kemeny-Young ranking
def Kemeny_Young(pairwise_ballot, N_candidates, candidate_order):

    #score all possible rankings
    all_rankings=list(itertools.permutations(range(N_candidates)))
    score_table = []
    
    for ranking in all_rankings:  #ex [1,0,2] which represents [ 'Cardi', ' Bruno', 'Rocky']
        score=0
        for runner_index in range(N_candidates):  #ex position 0, which holds candidate 1 
            opponent_index = runner_index
            while opponent_index < N_candidates-1:
                opponent_index += 1
                runner = ranking[runner_index]
                opponent = ranking[opponent_index]
                score += int(pairwise_ballot[runner, opponent]) #add number of voters who preferred runner over opponent, retrieved from summed ballot
        score_table.append(score)
    
#decide winner
    final_ranking = []
    for score_index in range(len(score_table)):
        if score_table[score_index] == int(max(score_table)):
            final_ranking.append(all_rankings[score_index]) 

#interpret results
    final_ranking_names = []
    
    if len(final_ranking) > 1:
        print('There is a tie')
        
    for ranking in final_ranking:
        each_final_ranking_names = []
        for i in ranking:
            each_final_ranking_names.append(candidate_order[i])
        final_ranking_names.append(each_final_ranking_names)
    
    print('Final ranking(s) : ', final_ranking_names)
    return(final_ranking_names)

###########################################################################
###########################################################################
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
    
#####################################################
x=reduce_votes(votes, len(candidate_order))
Kemeny_Young(x[0], x[1], candidate_order)
