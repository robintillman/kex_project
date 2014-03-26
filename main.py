import sys
import wikipedia
import re


def flesch_kincaid(wor, sen, syl):
    result = 0.39 * (wor/sen) + 11.8 * (syl/wor) - 15.59
    print result
    
    
def get_values(wiki_text):
    text = re.sub(r'[^\x00-\x7F]+',' ', wiki_text) # replace non-ascii characters
    text = re.sub(r'[\n]+', '', text) # replace newlines
    text = re.split("==+ \w+[ \w+]* ==+", text) # get paragraphs using regex
     
    #print text
       
    sentences = get_sentences(text)
    words = get_words(text)
    syllables = get_syllables(text)
    
    return sentences, words, syllables
    
def get_sentences(text):
    sentences_reg = re.split("[.!?]", text) # get sentences using regex
    return len(sentences_reg)
    
    
def get_words(sentence):
    words_reg = re.split("[ ]", sentence)
    return len(words_reg)
    
    
def get_syllables(word):
    syllables_reg = re.split("[aeuio]", word)
    return len(syllables_reg)
    
def main():
    wiki_text = wikipedia.page("Flesch-Kincaid").content
    sentences, words, syllables = get_values(wiki_text)
    
    result = flesch_kincaid(sentences, words, syllables)
    
if  __name__ =='__main__':main()
