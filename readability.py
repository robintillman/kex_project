import sys
import re
import io
import wikipedia
import translate
import json
import nationsArray


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
    
def calc_darwin():
    en_version = open('texts/darwinEN.txt', 'r')
    sv_version = open('texts/darwinSV.txt', 'r')
    
    # Read files, return string
    en = en_version.read()
    sv = sv_version.read()
    
    # Clean strings
    en = clean_text(en)
    sv = clean_text(sv)
    
    # Calc parameters
    en_chars = character_count(en)
    en_words = word_count(en)
    en_sents = sentence_count(en)
    en_longs = long_word_count(en)
        
    sv_chars = character_count(sv)
    sv_words = word_count(sv)
    sv_sents = sentence_count(sv)
    sv_longs = long_word_count(sv)
    
    print("EN CHARS: ", en_chars, " EN WORDS: ", en_words, " EN SENTS: ", en_sents, " EN LONGS: ", en_longs)
    print("SV CHARS: ", sv_chars, " SV WORDS: ", sv_words, " SV SENTS: ", sv_sents, " SV LONGS: ", sv_longs)    
    
    # Calc indexes
    EN_CLI = CLI(en_chars, en_words, en_sents)
    EN_ARI = ARI(en_chars, en_words, en_sents)
    EN_LIX = LIX(en_words, en_sents, en_longs)

    SV_CLI = CLI(sv_chars, sv_words, sv_sents)
    SV_ARI = ARI(sv_chars, sv_words, sv_sents)
    SV_LIX = LIX(sv_words, sv_sents, sv_longs)   
    
    print()
    print("EN CLI: ", EN_CLI)
    print("EN ARI: ", EN_ARI)
    print("EN LIX: ", EN_LIX)
    print("SV CLI: ", SV_CLI)
    print("SV ARI: ", SV_ARI)
    print("SV LIX: ", SV_LIX)
    print()
    
def calc_bible():
    en_version = open('texts/bibleEN.txt', 'r')
    sv_version = open('texts/bibleSV.txt', 'r')
    
    # Read files, return string
    en = en_version.read()
    sv = sv_version.read()
    
    # Clean strings
    en = clean_text(en)
    sv = clean_text(sv)
    
    # Calc parameters
    en_chars = character_count(en)
    en_words = word_count(en)
    en_sents = sentence_count(en)
    en_longs = long_word_count(en)
        
    sv_chars = character_count(sv)
    sv_words = word_count(sv)
    sv_sents = sentence_count(sv)
    sv_longs = long_word_count(sv)    
    
    print("EN CHARS: ", en_chars, " EN WORDS: ", en_words, " EN SENTS: ", en_sents, " EN LONGS: ", en_longs)
    print("SV CHARS: ", sv_chars, " SV WORDS: ", sv_words, " SV SENTS: ", sv_sents, " SV LONGS: ", sv_longs)
        
    # Calc indexes
    EN_CLI = CLI(en_chars, en_words, en_sents)
    EN_ARI = ARI(en_chars, en_words, en_sents)
    EN_LIX = LIX(en_words, en_sents, en_longs)

    SV_CLI = CLI(sv_chars, sv_words, sv_sents)
    SV_ARI = ARI(sv_chars, sv_words, sv_sents)
    SV_LIX = LIX(sv_words, sv_sents, sv_longs)   
    
    print()
    print("EN CLI: ", EN_CLI)
    print("EN ARI: ", EN_ARI)
    print("EN LIX: ", EN_LIX)
    print("SV CLI: ", SV_CLI)
    print("SV ARI: ", SV_ARI)
    print("SV LIX: ", SV_LIX)
    print()   
    
def write_json_wiki():
    nations = nationsArray.nations
        
    EN_CLI = {}
    EN_ARI = {}
    EN_LIX = {}

    SV_CLI = {}
    SV_ARI = {}
    SV_LIX = {}
    
    translator = translate.Translator(to_lang="sv")

    for nation in nations:
        sv_nation = translator.translate(nation) # Gain swedish country name
       
        wikipedia.set_lang("en")
        en_text = wikipedia.page(nation).content # Gain english wikipedia text
        
        wikipedia.set_lang("sv")
        sv_text = wikipedia.page(sv_nation).content
        
        en_text = clean_text(en_text) # Parse and clean the wikipedia text
        sv_text = clean_text(sv_text) # Parse and clean the wikipedia text
        
            
        # Count needed parameters
        en_chars = character_count(en_text)
        en_words = word_count(en_text)
        en_sents = sentence_count(en_text)
        en_longs = long_word_count(en_text)
        
        sv_chars = character_count(sv_text)
        sv_words = word_count(sv_text)
        sv_sents = sentence_count(sv_text)
        sv_longs = long_word_count(sv_text)
        
        # Calculate and store readability scores
        EN_CLI[nation] = CLI(en_chars, en_words, en_sents)
        EN_ARI[nation] = ARI(en_chars, en_words, en_sents)
        EN_LIX[nation] = LIX(en_words, en_sents, en_longs)

        SV_CLI[nation] = CLI(sv_chars, sv_words, sv_sents)
        SV_ARI[nation] = ARI(sv_chars, sv_words, sv_sents)
        SV_LIX[nation] = LIX(sv_words, sv_sents, sv_longs)    

        data = [{'country': key, 'score': val} for key, val in EN_CLI.items()]
        json_string = json.dumps(data)
        with open('EN_CLI.json', 'w') as outfile:
            json.dump(json_string, outfile)
    
        data = [{'country': key, 'score': val} for key, val in EN_ARI.items()]
        json_string = json.dumps(data)
        with open('EN_ARI.json', 'w') as outfile:
            json.dump(json_string, outfile)
    
        data = [{'country': key, 'score': val} for key, val in EN_LIX.items()]
        json_string = json.dumps(data)
        with open('EN_LIX.json', 'w') as outfile:
            json.dump(json_string, outfile)
    
        data = [{'country': key, 'score': val} for key, val in SV_CLI.items()]
        json_string = json.dumps(data)
        with open('SV_CLI.json', 'w') as outfile:
            json.dump(json_string, outfile)
    
        data = [{'country': key, 'score': val} for key, val in SV_ARI.items()]
        json_string = json.dumps(data)
        with open('SV_ARI.json', 'w') as outfile:
            json.dump(json_string, outfile)
    
        data = [{'country': key, 'score': val} for key, val in SV_LIX.items()]
        json_string = json.dumps(data)
        with open('SV_LIX.json', 'w') as outfile:
            json.dump(json_string, outfile)    
            
def calc_average_wiki():
    nations = nationsArray.nations
    
    translator = translate.Translator(to_lang="sv")

    SV_CLI = 0
    SV_ARI = 0
    SV_LIX = 0
    EN_CLI = 0
    EN_ARI = 0
    EN_LIX = 0

    en_chars = 0
    en_words = 0
    en_sents = 0
    en_longs = 0
    sv_chars = 0
    sv_words = 0
    sv_sents = 0
    sv_longs = 0
    
    for nation in nations:
        sv_nation = translator.translate(nation) # Gain swedish country name
       
        wikipedia.set_lang("en")
        en_text = wikipedia.page(nation).content # Gain english wikipedia text
        
        wikipedia.set_lang("sv")
        sv_text = wikipedia.page(sv_nation).content
        
        en_text = clean_text(en_text) # Parse and clean the wikipedia text
        sv_text = clean_text(sv_text) # Parse and clean the wikipedia text
        
            
        # Count needed parameters
        en_chars_this = character_count(en_text)
        en_words_this = word_count(en_text)
        en_sents_this = sentence_count(en_text)
        en_longs_this = long_word_count(en_text)
        
        sv_chars_this = character_count(sv_text)
        sv_words_this = word_count(sv_text)
        sv_sents_this = sentence_count(sv_text)
        sv_longs_this = long_word_count(sv_text)
        
        EN_CLI += CLI(en_chars_this, en_words_this, en_sents_this)
        EN_ARI += ARI(en_chars_this, en_words_this, en_sents_this)
        EN_LIX += LIX(en_words_this, en_sents_this, en_longs_this)

        SV_CLI += CLI(sv_chars_this, sv_words_this, sv_sents_this)
        SV_ARI += ARI(sv_chars_this, sv_words_this, sv_sents_this)
        SV_LIX += LIX(sv_words_this, sv_sents_this, sv_longs_this)
        
        en_chars += en_chars_this
        en_words += en_words_this
        en_sents += en_sents_this
        en_longs += en_longs_this
        sv_chars += sv_chars_this
        sv_words += sv_words_this
        sv_sents += sv_sents_this
        sv_longs += sv_longs_this
        
    SV_CLI_AVG = SV_CLI / len(nations)
    SV_ARI_AVG = SV_ARI / len(nations)
    SV_LIX_AVG = SV_LIX / len(nations)
    EN_CLI_AVG = EN_CLI / len(nations)
    EN_ARI_AVG = EN_ARI / len(nations)
    EN_LIX_AVG = EN_LIX / len(nations)
    
    print("EN CHARS: ", en_chars, " EN WORDS: ", en_words, " EN SENTS: ", en_sents, " EN LONGS: ", en_longs)
    print("SV CHARS: ", sv_chars, " SV WORDS: ", sv_words, " SV SENTS: ", sv_sents, " SV LONGS: ", sv_longs)
  
    EN_CLI_TOTAL = CLI(en_chars, en_words, en_sents)
    EN_ARI_TOTAL = ARI(en_chars, en_words, en_sents)
    EN_LIX_TOTAL = LIX(en_words, en_sents, en_longs)
    
    print("EN CLI TOTAL: ", EN_CLI_TOTAL, " EN ARI TOTAL: ", EN_ARI_TOTAL, " EN LIX TOTAL: ", EN_LIX_TOTAL)

    SV_CLI_TOTAL = CLI(sv_chars, sv_words, sv_sents)
    SV_ARI_TOTAL = ARI(sv_chars, sv_words, sv_sents)
    SV_LIX_TOTAL = LIX(sv_words, sv_sents, sv_longs)
    
    print("SV CLI TOTAL: ", SV_CLI_TOTAL, " SV ARI TOTAL: ", SV_ARI_TOTAL, " SV LIX TOTAL: ", SV_LIX_TOTAL)
    
    print()
    print("EN CLI AVG: ", EN_CLI_AVG)
    print("EN ARI AVG: ", EN_ARI_AVG)
    print("EN LIX AVG: ", EN_LIX_AVG)
    print("SV CLI AVG: ", SV_CLI_AVG)
    print("SV ARI AVG: ", SV_ARI_AVG)
    print("SV LIX AVG: ", SV_LIX_AVG)
    print()
