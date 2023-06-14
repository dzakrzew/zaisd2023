"""
Algorytm wyszukiwania palindromów

Autor:  <@student.polsl.pl>
Data: 21-03-2023
"""

def palindromes(text):
    words = text.split()
    p = []
    for w in words:
        if w == w[::-1]:
            p.append(w)
    return p

text = "chciałbym zaraz pójść na kajak ale dzisiaj jest zakaz"
print(palindromes(text))