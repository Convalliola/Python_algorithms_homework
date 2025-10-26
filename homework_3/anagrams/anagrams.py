"""
Дан список слов. Сгруппируйте слова так, чтобы в одной группе оказались все анаграммы.
"""
alphabet = dict(zip('абвгдеёжзийклмнопрстуфхцчшщъыьэюя', range(0, 32)))

def word_to_table(word):
    table = [0] * 32
    for letter in word:
        table[alphabet[letter]] += 1
    return tuple(table)
        

def anagrams_(words):
    anagrams = {}
    for word in words:
        letters = word_to_table(word)
        if letters in anagrams:
            anagrams[letters].append(word)
        else:
            anagrams[letters] = [word]
    return anagrams.values()


