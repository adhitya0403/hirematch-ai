skill_set = [
    # Languages
    "python", "javascript", "typescript", "java", "c", "c++", "go", "rust","sql",

    # Frontend
    "react", "nextjs", "redux", "zustand",
    "html", "css", "tailwind", "bootstrap", "sass",
    "vite", "webpack",

    # Backend
    "node", "express", "fastapi", "django", "flask",
    "spring", "springboot",

    # Databases
    "postgresql", "mysql", "mongodb", "redis", "sqlite", "firebase",

    # APIs & Architecture
    "api", "rest", "graphql", "microservices", "websocket",

    # DevOps / Cloud
    "aws", "azure", "gcp", "docker", "kubernetes",
    "nginx", "vercel", "render", "netlify",

    # Tools
    "git", "github", "gitlab", "postman", "figma",
    "linux", "bash",

    # Testing
    "jest", "mocha", "chai", "pytest", "selenium",

    # Data / AI
    "pandas", "numpy", "tensorflow", "pytorch", "scikit"
]


normalization_map = {
    "apis": "api",
    "api": "api",
    "js": "javascript",
    "postgres": "postgresql",
    "nodejs": "node",
    "node.js": "node",
    "reactjs": "react",
    "react.js": "react",
}

SECTION_KEYWORDS = {
    "summary": ["summary", "profile"],
    "skills": ["skills", "technical skills","technologies"],
    "experience": ["experience", "work experience"],
    "projects": ["projects"],
    "education": ["education"],
    "cerfications" : ["certifications","achievements"]
}