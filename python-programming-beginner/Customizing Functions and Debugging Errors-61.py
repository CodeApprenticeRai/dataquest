## 3. Optional Arguments ##

# Default code
def tokenize(text_string, special_characters, clean=False):
    if clean == True:
        cleaned_story = clean_text(text_string, special_characters)
        story_tokens = cleaned_story.split(" ")
        return(story_tokens)
    else:
        story_tokens = cleaned_story.split(" ")
        return(story_tokens)
    

tokenized_story = tokenize(story_string, clean_chars, True)
tokenized_vocabulary = tokenize(vocabulary, clean_chars, True)
misspelled_words = []

for tk in tokenized_story:
    if tk in tokenized_vocabulary:
        pass
    else:
        misspelled_words.append(tk)
 

print(misspelled_words) 

## 5. Practice: Creating a More Compact Spell Checker ##

def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters, clean=False):
    cleaned_text = text_string
    if clean:
        cleaned_text = clean_text(text_string, special_characters)
    tokens = cleaned_text.split(" ")
    return(tokens)


final_misspelled_words = []
def spell_check(vocabulary_file, text_file, special_characters = [",",".","'",";","\n"]):
    misspelled_words = []
    vf = open(vocabulary_file).read()
    tf = open(text_file).read()
    tokenized_vocabulary = tokenize(vf, special_characters)
    tokenized_text = tokenize(tf, special_characters, True)
    for tkt in tokenized_text:
        if tkt not in tokenized_vocabulary and tkt != '':
            misspelled_words.append(tkt)
    return(misspelled_words)

final_misspelled_words = spell_check(vocabulary_file = "dictionary.txt", text_file = "story.txt")
print(final_misspelled_words)    

## 7. Syntax Errors ##

def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"]):
    misspelled_words = []
    vocabulary = open(vocabulary_file).read()
    text = open(text_file).read()
    
     tokenized_vocabulary = tokenize(vocabulary, special_characters)
    tokenized_text = tokenize(text, special_characters, True)
    
    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return(misspelled_words)

final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt")
print(final_misspelled_words)

## 11. Traceback ##

def spell_check(vocabulary_file, text_file, special_characters=[",",".","'",";","\n"]):
    misspelled_words = []
    vocabulary = open(vocabulary_file).read()
    # Add ending parentheses.
    text = open(text_file).read()
    
    # Fix indentation.
    tokenized_vocabulary = tokenize(vocabulary, special_characters)
    tokenized_text = tokenize(text, special_characters, True)
    
    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return(misspelled_words)

final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt", special_characters=1)
print(final_misspelled_words)