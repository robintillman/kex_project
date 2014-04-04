import sys
import re
import wikipedia
import translate


#   Coleman-Liau Index
def CLI(chars, words, sents):
    words = float(words)
    res = (5.88*(chars/words))-(29.6*(sents/words))-15.8 
    return res    
  
#   Automated Readability Index 
def ARI(chars, words, sents):
    words = float(words)
    res = (4.71*(chars/words))+(0.5*(words/sents))-21.43  
    return res
    
    
#   Lasbarhetsindex
def LIX(words, sents, longs):
    words = float(words)
    res = (words/sents) + (longs*100/words)
    return res
    

#   Clean text for easy parsing;
#   remove/replace unwanted characters etc.
def clean_text(text):
    # Remove wiki titles
    text = re.sub(r"==+ \w+[ \w+]* ==+", " ", text) # Merge paragraphs to one text
    text = re.sub(r"==+ \w+[\W \w+]* ==+", " ", text) # Merge paragraphs to one text

    # Curly quotes etc
    text = re.sub("\xe2\x80\x98", "'", text)
    text = re.sub("\xe2\x80\x99", "'", text)
    text = re.sub("\xe2\x80\x9c", '"', text)
    text = re.sub("\xe2\x80\x9d", '"', text)
    text = re.sub("\xe2\x80\x93", "-", text)
    text = re.sub("\xe2\x80\x94", "--", text)
    text = re.sub("\xe2\x80\xa6", "...", text) 
    text = re.sub(chr(145), "'", text)
    text = re.sub(chr(146), "'", text)
    text = re.sub(chr(147), '"', text)
    text = re.sub(chr(148), '"', text)
    text = re.sub(chr(150), "-", text)
    text = re.sub(chr(151), "--", text)
    text = re.sub(chr(133), "...", text)
    text = re.sub("'", "", text)
    
    # Replace commas, hyphens, quotes etc (count as spaces)
    text = re.sub('[",:;()/\-]', " ", text);
    
    # Remove newlines (count as spaces)
    text = re.sub("\n", " ", text)
    
    # Unify terminators
    text = re.sub("[\.!?]", ".", text)
    
    # Check for duplicate terminators
    text = re.sub("\.\.+", ".", text)
    
    # Remove numeric values
    text = re.sub("[0-9]+.?[0-9]*", "", text)
    
    # Remove overflow spaces
    text = re.sub("[ ]+", " ", text)
    text = re.sub(" +\.", ".", text)
    
    # Remove unwanted non-ascii characters
    text = re.sub(" \W+ ", " ", text)
    
    
    # Add "." to end if not existing
    if text[len(text)-1] != ".": 
        text += "."
    
    return text 
    
    
#   After cleaning text the number of words are equal to
#   the amount of spaces + 1.
def word_count(text):    
    res = text.count(" ") + 1
    return res


#   After cleaning text the number of sentences are equal to
#   the amount of dots. The result will be tripped by
#   occurences of shortened words such as "U.S" or "Mr. ". 
#   However this will not have a very big impact on the result.
def sentence_count(text):    
    res = text.count(".")
    return res


#   Remove all spaces and other non-characters
#   and the length of the remaining string will
#   be equal to the amount of characters 
def character_count(text):
    res = len(re.sub("[\. \W]+", "", text))
    return res


#   LIX use the amount of long words in its formula
#   (a long word is defined as a word with more than
#   6 characters)
def long_word_count(text):
    text = re.sub("\.", "", text)
    word_list = text.split(" ")
    res = 0;
    for word in word_list:
        if len(word) > 6:
            res += 1
    
    return res
    
    
def main():
    langs = ["en","sv"]
    countries = ["Sweden", "Germany", "Spain", "France", "Russia"] 
    
    for lang in langs:
        print()
        print("------------" + lang.upper() + "------------")
        wikipedia.set_lang(lang) # Set language
        translator = translate.Translator(to_lang=lang)
        
        for country in countries:
            print()
            translation = translator.translate(country)
            text = wikipedia.page(translation).content
            print(" .........." + translation.upper() + "..........")
            
            cleaned_text = clean_text(text)
            
            chars = character_count(cleaned_text)
            words = word_count(cleaned_text)
            sents = sentence_count(cleaned_text)
            longs = long_word_count(cleaned_text)
            
            print(" CLI: " + str(CLI(chars, words, sents)))
            print(" ARI: " + str(ARI(chars, words, sents)))
            print(" LIX: " + str(LIX(words, sents, longs)))
    
if  __name__ =='__main__':main()   
