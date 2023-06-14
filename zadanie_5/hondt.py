"""
Algorytm Hondt

Autor:  <@student.polsl.pl>
Data: 02-04-2023
"""

def dhondt(votes, seats):
    results = [0] * len(votes)
    q = [votes[i] / (1 + results[i]) for i in range(len(votes))]
    
    for _ in range(seats):
        max_value = max(q)
        max_index = q.index(max_value)
        results[max_index] += 1
        q[max_index] = votes[max_index] / (1 + results[max_index])
        
    return results

votes = [720, 300, 480]
seats = 8
print(dhondt(votes, seats))