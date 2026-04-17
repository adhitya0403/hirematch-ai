from fastapi import FastAPI
from services.analyzer import analyzer
from services.tokenizer import tokenizer
import json

resume_text = '''React.js , react js
'''

jd_text = ''' We are looking for a Backend Developer.

Requirements:

- Strong knowledge of Python
- Experience with SQL and databases
- Familiarity with Docker and APIs

Nice to have:

- AWS experience 
- React js
'''


app = FastAPI()

@app.get("/")
def home():
    return {"Message":"Home"}

@app.get("/analyze")
def analyze():
 return analyzer(resume_text,jd_text)

