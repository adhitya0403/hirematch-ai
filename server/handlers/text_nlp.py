from config.keywords import normalization_map
import spacy

nlp = spacy.load("en_core_web_sm")

def tokenizer(text):
    doc = nlp(text)
    tokens = []
    for token in doc:
        if not token.is_punct and not token.is_space and not token.is_stop:
            tokens.append(token.lemma_.lower())
    return tokens
    

def normalizer(token):
    return normalization_map.get(token, token)