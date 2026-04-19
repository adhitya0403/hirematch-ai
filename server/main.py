from fastapi import FastAPI
from services.analyzer import analyzer
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File, Form
from utils.get_text import get_text


resume_text = '''Adhitya Darshanala
Hyderabad|Email:darshanalaadhitya@gmail.com |Mobile:+91 7396498913 | LinkedIn|GitHub | Portfolio
Summary
Full-stack developer experienced in building responsive web applications and scalable backend systems. Skilled in
developing interactive user interfaces with React and designing efficient APIs using Node.js and Express. Comfortable
working with both SQL and NoSQL databases, with a focus on performance and clean architecture.
Projects
TypeRush — Real-Time Multiplayer Typing Platform (MERN, Socket.IO, Web Speech API) GitHub | Live
• Built a real-time multiplayer system with synchronized game state using WebSockets
• Developed interactive frontend using React, Zustand, and Tailwind for responsive user experience
• Designed backend APIs and event-driven communication for real-time updates
• Implemented multiple game modes with custom logic and input validation
• Managed user profiles, session stats, and application state efficiently
Notify — Task & Notes Management Platform (MERN) GitHub | Live
• Developed a full-stack application with JWT-based authentication and user-specific data handling
• Designed RESTful APIs for managing tasks and notes with proper error handling
• Improved frontend performance by reducing unnecessary API calls and optimizing state updates
E-Commerce Website — React Web App GitHub | Live
• Built an interactive e-commerce interface with product listing, cart management, and checkout workflows
• Designed modular and reusable UI components for scalable and maintainable frontend architecture
• Implemented dynamic product interactions and real-time cart updates to enhance user experience
RESTful APIs — Backend Development & Integration
• Random API: Delivered quotes in lowercase, uppercase, and mixed formats for quick app integration. GitHub | Live
• Product API: Provided endpoints to fetch all products or a single product by ID with sorted responses. GitHub | Live
Technologies
Languages: JavaScript, C++
Frontend: React.js, HTML, CSS, Tailwind
Backend: Node.js, Express.js
Databases: PostgreSQL, MongoDB, SQL
Tools: Git, GitHub, Postman, AWS, Vercel, Render, Figma
Core Skills: Full-Stack Development, REST APIs, CRUD Operations, State Management, Component-Based Architecture,
Responsive Web Design, Problem Solving (DSA)
Education
Siddhartha Institute of Technology and Sciences 2022 – 2026
• Bachelor of Technology - Computer Science Engineering
• GPA: 8/10
Alphores Junior College 2020 – 2022
• Intermediate Board of Education - Mathematics, Physics and Chemistry
• GPA: 9.8/10
Certifications & Achievements
• Front-End Development Libraries - freeCodeCamp
• Node.js and Express.js Basics - freeCodeCamp
• Solved 100+ algorithmic problems on LeetCode, strengthening DSA and problem-solving skills. LeetCode
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

@app.get("/")
def home():
    return {"Message":"Home"}

@app.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    jd_file: UploadFile = File(None),
    jd_text: str = Form(None),
    role: str = Form(None)
):
    try:
        #resume file
        resume_text = await get_text(file=resume)

        # jd can be file OR text
        jd_text = await get_text(file=jd_file, text=jd_text)

        return {
            "resume_text": resume_text[:1000],  # preview
            "jd_text": jd_text[:1000] if jd_text else None,
            "role": role,
        }


    except Exception as e:
        return {"error": str(e)}

