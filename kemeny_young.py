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
    for ranking in final_ranking:
        each_final_ranking_names = []
        for i in ranking:
            each_final_ranking_names.append(candidate_order[i])
        final_ranking_names.append(each_final_ranking_names)    

#handle ties          #ties where rankings have different winners are resolved by determining the winner that has the highest score over all other candidates
    tie=False
    if len(final_ranking) > 1:
        tie=True

        tied_winners = []
        for tied_ranking in final_ranking: #ex [2,1,0]
            tied_winners.append(tied_ranking[0]) #ex candidate 2
            tied_winners=list(set(tied_winners)) #remove duplicates

        tie_score_table = []
        for runner in tied_winners:  #ex candidate 2
            tie_score = 0
            opponent_list = list(range(N_candidates))
            opponent_list.remove(runner)
            for opponent in opponent_list:
                tie_score += int(pairwise_ballot[runner, opponent]) #add number of voters who preferred runner over opponent, retrieved from summed ballot
        tie_score_table.append(tie_score)

        tie_breaker = []
        for tie_score_index in range(len(tie_score_table)):
            if tie_score_table[tie_score_index] == int(max(tie_score_table)):
                tie_breaker.append(tied_winners[tie_score_index])   


    #interpret tie
        tie_breaker_name = []
    
        for winner in tie_breaker:
            tie_breaker_name.append(candidate_order[winner])

    
    print('Final ranking(s) : ', final_ranking_names)
    print(final_ranking)
    print(pairwise_ballot)
    #print(tied_winners)
    #print(tie_breaker)
    #print(tie_breaker_name)
    
    output={'finalRankingNames':final_ranking_names, 'finalRanking': final_ranking, 'tie': tie}
    if tie == True:
        output['finalWinner'] = tie_breaker_name
        
    return(output)


