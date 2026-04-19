from config.keywords import SECTION_KEYWORDS

def get_section(line):
    clean = line.strip().lower()

    for section, keywords in SECTION_KEYWORDS.items():
        for keyword in keywords:
           if clean.startswith(keyword) and len(clean.split()) <= 5:
                print(section)
                return section

    return None