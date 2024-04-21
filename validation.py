def word_variations_count(total_words, selected_count):
    return total_words ** selected_count

# Example usage:
total_words = 4
selected_count = 3

result = word_variations_count(total_words, selected_count)
print(result)

words_list = [
    "word2",
    "word4word2word3word1",
    "word2word1word4word3",
    "word3word4word1word2",
    "word3word1word4word2",
    "word1word2word4word3",
    "word1_word2_word3_word4",
    "word4word3word2word1",
    "word4",
    "word2word4word3word1",
    "word3word1word2word4",
    "word4word1word3word2",
    "word1word3word4word2",
    "word4word3word1word2",
    "word1word4word2word3",
    "word1word4word3word2",
    "word2word4word1word3",
    "word4word1word2word3",
    "word3word4word2word1",
    "word3",
    "word3word2word4word1",
    "word1word3word2word4",
    "word2word3word1word4",
    "word1word2word3word4",
    "word2word1word3word4",
    "word2word3word4word1",
    "word3word2word1word4",
    "word4word2word1word3",
    "word1"
]

def has_duplicates(lst):
    seen = set()
    for word in lst:
        if word in seen:
            return True
        seen.add(word)
    return False

if has_duplicates(words_list):
    print("Duplicates found in the list.")
else:
    print("No duplicates found in the list.")
