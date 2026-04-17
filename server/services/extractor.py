from services.tokenizer import tokenizer
from config.keywords import skill_set
from services.normalizer import normalizer

def extractor(text):
    tokens = tokenizer(text)
    cleaned = set()
    for token in tokens:
        normalized = normalizer(token)
        if normalized in skill_set:
            cleaned.add(normalized)
    return cleaned