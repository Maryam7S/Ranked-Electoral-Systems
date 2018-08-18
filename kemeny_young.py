#Kemeny-Young method of voting
#The kemeny-young method is a condorcet method of voting. It satisfies the criterias
#of unrestricted domain and pareto efficiency but fails independence of irrelevant alternatives

import itertools

#DEFINE function to determine Kemeny-Young ranking
def kemeny_young(pairwise_ballot, N_candidates, candidate_order):

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


