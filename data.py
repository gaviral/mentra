import sqlite3
import os
import json

# Path to SQLite database
DB_PATH = "data/job_descriptions.db"

def init_db():
    """Initialize the database with sample job descriptions"""
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create job descriptions table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS job_descriptions (
        id INTEGER PRIMARY KEY,
        title TEXT,
        company TEXT,
        content TEXT,
        category TEXT
    )
    ''')
    
    # Check if table is empty
    cursor.execute("SELECT COUNT(*) FROM job_descriptions")
    count = cursor.fetchone()[0]
    
    # Insert sample data if empty
    if count == 0:
        sample_jobs = [
            {
                "title": "Software Engineer",
                "company": "Tech Solutions Inc.",
                "content": """We are looking for a Software Engineer with 3+ years of experience in Python and web development. The ideal candidate will have experience with modern web frameworks, API development, and database design. 

Responsibilities:
- Develop and maintain web applications using Python and Django/Flask
- Write clean, efficient, and well-documented code
- Collaborate with frontend developers to integrate user-facing elements
- Optimize applications for maximum speed and scalability
- Implement security and data protection measures

Requirements:
- Bachelor's degree in Computer Science or related field
- 3+ years of experience with Python development
- Experience with web frameworks (Django, Flask)
- Knowledge of database systems (SQL, NoSQL)
- Familiarity with frontend technologies (HTML, CSS, JavaScript)
- Strong problem-solving skills and attention to detail""",
                "category": "Technology"
            },
            {
                "title": "Data Scientist",
                "company": "Analytics Co.",
                "content": """We're seeking a Data Scientist with a strong background in machine learning and statistics to join our growing analytics team. The successful candidate will work on challenging problems and help transform raw data into actionable insights.

Responsibilities:
- Design and implement machine learning models
- Perform statistical analysis on large datasets
- Develop data visualizations to communicate findings
- Collaborate with engineering teams to implement models
- Stay current with latest ML research and techniques

Requirements:
- Master's degree or PhD in Computer Science, Statistics or related field
- 2+ years of experience in data science or machine learning
- Proficiency in Python and data science libraries (pandas, scikit-learn)
- Experience with deep learning frameworks (TensorFlow, PyTorch)
- Strong mathematical background in statistics and algorithms
- Excellent communication skills to present technical findings to non-technical stakeholders""",
                "category": "Data Science"
            },
            {
                "title": "Product Manager",
                "company": "Product Innovations",
                "content": """We are hiring a Product Manager with experience in agile methodologies and product lifecycle management. The ideal candidate will be passionate about creating user-centered products and driving their development from concept to launch.

Responsibilities:
- Define product strategy and roadmap
- Gather and prioritize user requirements
- Work closely with engineering, design, and marketing teams
- Define success metrics and track product performance
- Conduct competitive analysis and market research

Requirements:
- Bachelor's degree in Business, Computer Science, or related field
- 3+ years of experience in product management
- Experience with agile development methodologies
- Strong analytical and problem-solving skills
- Excellent communication and leadership abilities
- Technical background or understanding preferred""",
                "category": "Product"
            }
        ]
        
        for job in sample_jobs:
            cursor.execute(
                "INSERT INTO job_descriptions (title, company, content, category) VALUES (?, ?, ?, ?)",
                (job["title"], job["company"], job["content"], job["category"])
            )
    
    conn.commit()
    conn.close()

def get_job_descriptions():
    """Retrieve all job descriptions from the database"""
    # Initialize DB if needed
    if not os.path.exists(DB_PATH):
        init_db()
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM job_descriptions")
    jobs = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return jobs

def get_job_by_id(job_id):
    """Get a specific job description by ID"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM job_descriptions WHERE id = ?", (job_id,))
    result = cursor.fetchone()
    
    if result is None:
        conn.close()
        return None
    
    job = dict(result)
    
    conn.close()
    return job 