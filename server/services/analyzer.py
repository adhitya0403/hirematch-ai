from services.extractor import extractor

def analyzer(resume_text, jd_text=None, role=None):

    if jd_text:
        return {
            "mode": "compare",
            "message": "Comparing resume with JD",
            "resume_preview": resume_text[:200],
            "jd_preview": jd_text[:200],
        }

    return {
        "mode": "resume_only",
        "message": f"Analyzing resume for role: {role}",
        "resume_preview": resume_text[:200],
    }