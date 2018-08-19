#!/usr/bin/env python3
###########shebang line, tells shell what to do with file


#Kemeny-Young method of voting
#The kemeny-young method is a condorcet method of voting. It satisfies the criterias
#of unrestricted domain and pareto efficiency but fails independence of irrelevant alternatives

from numpy import *
import csv
import sys
from reduce_votes import reduce_votes
from kemeny_young import kemeny_young

###########################################################################
#imagine that an organization is voting on a candidate to fill a vacancy on its board of directors
with open('cast votes.csv', 'r') as f: #import votes from CSV file
    reader = csv.reader(f, delimiter=' ')
    votes = []
    for row in reader:
        votes.append(row)

with open('candidate list.txt') as f: #import candidate order from txt file
    for line in f:
        candidate_order = line.split(' ')
    
#####################################################
x=reduce_votes(votes, len(candidate_order))
kemeny_young(x[0], x[1], candidate_order)
