from services.extractor import extractor

def analyzer(resume_text,jd_text,skill_set):
    resume_words = extractor(resume_text.lower(),skill_set)
    jd_words = extractor(jd_text.lower(),skill_set)
    resume_set = set(resume_words)
    jd_set = set(jd_words)
    matched = jd_set & resume_set
    not_matched = jd_set - resume_set
    return {
        "matched" : matched,
        "not_matched" : not_matched,
        "score" : len(matched)/len(jd_set)
    }