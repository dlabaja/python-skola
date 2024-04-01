def transform_words(words):
    transform_word = lambda word: word.upper() + str(len(word))

    transformed_words = map(transform_word, words)

    return list(transformed_words)
