import spacy
from config.keywords import skill_set

nlp = spacy.load("en_core_web_sm")

def tokenizer(text):
    doc = nlp(text)
    tokens = []
    for token in doc:
        if not token.is_punct and not token.is_space and not token.is_stop:
            tokens.append(token.lemma_.lower())
    print(tokens)
    return tokens
    
    
    