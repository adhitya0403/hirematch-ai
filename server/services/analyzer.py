from services.extractor import extractor

def analyzer(resume_text,jd_text):
    resume_set = extractor(resume_text)
    # matched = jd_set & resume_set
    # not_matched = jd_set - resume_set
    # return {
    #     "matched" : matched,
    #     "not_matched" : not_matched,
    #     "score" : len(matched)/len(jd_set)
    # }
    return {
        "resume_set" : resume_set,
    }