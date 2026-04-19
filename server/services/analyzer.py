from handlers.extractors import extract_sections


def analyzer(resume_text, jd_text=None, role=None):

    resume_sections = extract_sections(resume_text)

    jd_processed = None
    if jd_text:
        jd_processed = extract_sections(jd_text)

    return {
        "resume_sections": resume_sections,
        "jd_set": jd_processed if jd_text else None,
        "role": role,
    }