#!/usr/bin/env python3  #shebang line, tells shell what to do with file

#Kemeny-Young method of voting
#The kemeny-young method is a condorcet method of voting. It satisfies the criterias
#of unrestricted domain and pareto efficiency but fails independence of irrelevant alternatives

from numpy import *
import random
import itertools

#################################################
#DEFINE function to determine Kemeny-Young ranking
def reduce_votes(votes, can_list):

#initialize
    N_candidates = len(can_list)
    N_pairs = int(((N_candidates**2) - N_candidates)/2)
    pairs = []  #determine all possible set of pairs
    for a in range(N_candidates):
        n= a + 1
        while n < N_candidates:
            pairs.append([a,n])
            n=n+1

#create pair-wise preference matrix 
    PPM = zeros([N_pairs,3]) 
    for p in pairs:
        for v in range(N_voters):
            if votes[v,p[0]] > votes[v,p[1]]: #prefer X over Y
                PPM[pairs.index(p),0]= PPM[pairs.index(p),0]+1
            elif votes[v,p[0]] == votes[v,p[1]]: #equal preference
                PPM[pairs.index(p),1] = PPM[pairs.index(p),1] + 1
            elif votes[v,p[0]] < votes[v,p[1]]: #prefer Y over X
                PPM[pairs.index(p),2] = PPM[pairs.index(p),2] +1

    #score all possible rankings
    all_rankings=list(itertools.permutations(can_list))
    
    deltas = [0] #list of intervals of increase of our index list
    for i in range(N_candidates-2):
        deltas.append(N_candidates-i-1)
    index=[0] #indices for our score table, to locate starting point of each candidate's list of comparisons
    for i in range(len(deltas)-1):
        index.append(index[i]+deltas[i+1])

    score_table = []
    for ranking in all_rankings:
        score=0
        for i in range(len(ranking)):
            b=i
            while b < N_candidates - 1:
                b=b+1
                if ranking[i]>ranking[b]:    
                    score = score + PPM[(index[i] + b-i-1) ,0]
                else:
                    score = score + PPM[(index[i] + b-i-1) ,2]
        score_table.append(score)
    
#decide winner
    winner = all_rankings[score_table.index(max(score_table))]
    print('Final ranking is', winner)

###########################################################################
###########################################################################
    
#imagine that an organization is voting on a candidate to fill a vacancy on its board of directors
#the candidates' names are Bruno, Cardi, Rocky, Travis, Donald
can_list = ['Bruno', 'Cardi', 'Rocky', 'Travis', 'Donald']   #replace with dict
N_candidates = len(can_list)
ballot = zeros(N_candidates)

#assign random votes
N_voters = 40 #number of voters
votes = zeros([N_voters, N_candidates])
for i in range(N_voters):
    for a in range (N_candidates):
        ballot[a]= random.randint(1, 5) 
    votes[i]=ballot

reduce_votes(votes, can_list)
