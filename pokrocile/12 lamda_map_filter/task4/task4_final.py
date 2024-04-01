def complex_word_filter(words, min_length):
    filter_by_length = lambda word: len(word) > min_length

    transform_word = lambda word: word.upper() + str(
        word.lower().count('a') + word.lower().count('e') + word.lower().count('i') + word.lower().count(
            'o') + word.lower().count('u'))

    filtered_and_transformed_words = map(transform_word, filter(filter_by_length, words))

    return list(filtered_and_transformed_words)

