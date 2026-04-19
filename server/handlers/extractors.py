from handlers.text_nlp import tokenizer
from config.keywords import skill_set
from handlers.text_nlp import normalizer
from utils.get_section import get_section

text = '''

summary
i am Adhitya klfklsflkasflsdhldfshkldsklsd
albeto del rio

projects
weather app, calculator
simple english

'''

#sections extraction
def extract_sections (text):
    lines = text.strip().split("\n")
    
    lines = [line.strip() for line in lines if line.strip()]
    
    sections ={}
    current_section = None
    
    for line in lines:
        section_name = get_section(line)
        
         # if header found → switch
        if section_name:
            current_section = section_name
            sections[current_section] = []
            continue

        # otherwise → add content
        if current_section:
            sections[current_section].append(line)
            
    return sections
    
#experience
def extract_experience () :
    pass

#projects
def extract_projects ():
    pass

#skills extractor
def extract_skills (text):
    tokens = tokenizer(text)
    cleaned = set()
    for token in tokens:
        normalized = normalizer(token)
        if normalized in skill_set:
            cleaned.add(normalized)
    return cleaned

#education
def extract_education():
    pass

#certifications & achievements
def extract_certifications():
    pass


    