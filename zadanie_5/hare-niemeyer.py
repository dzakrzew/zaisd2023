"""
Algorytm Hare-Niemeyer

Autor:  <@student.polsl.pl>
Data: 02-04-2023
"""

def hare_niemeyer(votes, seats):
    total_votes = sum(votes)
    quotas = [votes[i] * seats / total_votes for i in range(len(votes))]
    floor_quotas = [int(q) for q in quotas]
    results = floor_quotas.copy()
    remaining_seats = seats - sum(results)
    
    if remaining_seats > 0:
        fractions = [(quotas[i] - floor_quotas[i], i) for i in range(len(votes))]
        fractions.sort(reverse=True)
        for _, i in fractions[:remaining_seats]:
            results[i] += 1

    return results

# Mamy komitety A, B oraz C, które otrzymały kolejno 720, 300 i 480 głosów, do obsadzenia jest 8 mandatów.
votes = [720, 300, 480]
seats = 8
print(hare_niemeyer(votes, seats))