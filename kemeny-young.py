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
def reduce_votes(votes, can_list):

    N_candidates = len(can_list)
    pairwise_ballot=zeros([N_candidates, N_candidates]) #rows represent runners, columns represent opponents
    for ballot in votes:
        for a in range(N_candidates):
            for b in range(N_candidates):
                if a != b:
                    if ballot[a]>ballot[b]:
                        pairwise_ballot[a,b] +=1
    return(pairwise_ballot, can_list, N_candidates) 

#################################################
#DEFINE function to determine Kemeny-Young ranking
def Kemeny_Young(pairwise_ballot, can_list, N_candidates):

    #score all possible rankings
    all_rankings=list(itertools.permutations(can_list))
    print(all_rankings)
    
    score_table = []
    for ranking in all_rankings:  #ex [' Bruno', 'Cardi', 'Rocky']
        score=0
        ranking_indices=[]
        
        for a in ranking: #ex 'Bruno'
            ranking_indices.append(can_list.get(a))
        for i in range(N_candidates):
            b=i
            while b < N_candidates-1:
                b += 1
                score = int(score+pairwise_ballot[ranking_indices[i], ranking_indices[b]]) #add number of voters who preferred i over b
        score_table.append(score)
    print(score_table)
    
#decide winner
    Max = int(max(score_table))
    final_ranking = []
    for m in range(len(score_table)):
        if score_table[m] == Max:
            final_ranking.append(all_rankings[m]) 

    if len(final_ranking) > 1:
        print('There is a tie')
    
    print('Final ranking(s)', final_ranking)
    return(final_ranking)

###########################################################################
###########################################################################
#imagine that an organization is voting on a candidate to fill a vacancy on its board of directors
#the candidates' names are Bruno, Cardi, Rocky, Travis, Donald
can_list = {'Bruno': 0, 'Cardi': 1, 'Rocky': 2}   #replace with dict
N_candidates = len(can_list)

#assign random votes
N_voters = 10 #number of voters
votes = zeros([N_voters, N_candidates])
ballot = zeros(N_candidates)
for i in range(N_voters):
    for a in range (N_candidates):
        ballot[a]= random.randint(1, 5) 
    votes[i]=ballot
    
#####################################################
x=reduce_votes(votes, can_list)
Kemeny_Young(x[0], x[1], x[2])
