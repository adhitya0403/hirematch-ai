from fastapi import FastAPI
from services.analyzer import analyzer
import json

resume_text = ''' John Doe

Skills:
Python, FastAPI, SQL

Experience:
Built REST APIs using FastAPI and PostgreSQL.
Worked on backend systems.

Projects:
Developed a task manager using Python and React. 
'''

jd_text = ''' We are looking for a Backend Developer.

Requirements:

- Strong knowledge of Python
- Experience with SQL and databases
- Familiarity with Docker and APIs

Nice to have:

- AWS experience 
'''

with open("config/skill_set.json") as f:
    skill_set = json.load(f)

app = FastAPI()

@app.get("/")
def home():
    return {"Message":"Home"}

@app.get("/analyze")
def analyze():
    return analyzer(resume_text,jd_text,skill_set)

