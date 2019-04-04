word_to_count = {}
text = input("Text: ")
# splits words in words
words = text.split()
# Count ever time a word occurrces in text
for word in words:
    occurrence = word_to_count.get(word, 0)
    word_to_count[word] = occurrence + 1

words = list(word_to_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))
