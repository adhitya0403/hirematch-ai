

def extractor(text,skill_set):
    current = []
    for skill in skill_set:
        if skill in text:
            current.append(skill)
    return current;
            