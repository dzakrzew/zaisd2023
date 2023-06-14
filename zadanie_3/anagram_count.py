"""
Algorytm wyszukiwania anagramów poprzez zliczanie liter z użyciem słownika

Autor:  <@student.polsl.pl>
Data: 21-03-2023
"""

def count_chars(word):
    char_counts = {}
    for char in word:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def anagrams(text):
    words = text.split()
    anagrams = {}

    for w in words:
        word_counts = frozenset(count_chars(w).items())

        if word_counts in anagrams:
            anagrams[word_counts].append(w)
        else:
            anagrams[word_counts] = [w]
    return [words for words in anagrams.values() if len(words) > 1]

text = "kebab arak kara dzielenia test babke krab drab bard niedziela"
print(anagrams(text))