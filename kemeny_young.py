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

#handle ties    
    if len(final_ranking) > 1:
        tie=True
        print('There is a tie')

        tied_winners = []
        for i in range(len(final_ranking)):
            tied_winners.append(final_ranking[i][0])
            tied_winners=list(set(tied_winners))

        tie_score_table = []
        for runner in tied_winners:  #ex position 0, which holds candidate 1
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
        final_winner = []
    
        for winner in tie_breaker:
            final_winner.append(candidate_order[winner])


    
    print('Final ranking(s) : ', final_ranking_names)
    print(final_ranking)
    print(pairwise_ballot)
    print(tied_winners)
    print(tie_breaker)
    print(final_winner)
    return(final_ranking_names, tied_winners, final_winner)


