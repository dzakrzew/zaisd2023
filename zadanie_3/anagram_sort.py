"""
Algorytm wyszukiwania anagramów poprzez sortowanie liter z użyciem słownika

Autor:  <@student.polsl.pl>
Data: 21-03-2023
"""

def anagrams(text):
    words = text.split()
    anagrams = {}

    for w in words:
        sorted_word = "".join(sorted(w))

        if sorted_word in anagrams:
            anagrams[sorted_word].append(w)
        else:
            anagrams[sorted_word] = [w]
    
    return [words for words in anagrams.values() if len(words) > 1]

text = "kebab arak kara dzielenia test babke krab drab bard niedziela"
print(anagrams(text))