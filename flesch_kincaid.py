def flesch_kincaid(words, sentences, syllables):
    result = 0.39 * (words/sentences) + 11.8 * (syllables/words) - 15.59
    print(result)
