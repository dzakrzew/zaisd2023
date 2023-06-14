"""
Algorytm Sainte-Lague

Autor:  <@student.polsl.pl>
Data: 02-04-2023
"""

def sainte_lague(votes, seats):
    divisors = [1] * len(votes)
    results = [0] * len(votes)
    
    for _ in range(seats):
        max_value = -1
        max_index = -1

        for i, vote in enumerate(votes):
            value = vote / divisors[i]

            if value > max_value:
                max_value = value
                max_index = i
        
        results[max_index] += 1
        divisors[max_index] += 2

    return results

# Mamy komitety A, B oraz C, które otrzymały kolejno 720, 300 i 480 głosów, do obsadzenia jest 8 mandatów.
votes = [720, 300, 480]
seats = 8

print(sainte_lague(votes, seats))