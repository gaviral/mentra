# Core analysis prompt template
ANALYSIS_TEMPLATE = """
You are an expert resume coach helping job seekers improve their applications.

Please compare this resume:
---
{resume}
---

To this job description:
---
{job_description}
---

Provide a comprehensive analysis with the following sections:

1. QUALIFICATION: Is this person qualified for the position? (Yes/No) Explain your reasoning.

2. MISSING REQUIREMENTS: What important requirements from the job description are not addressed in the resume? List the specific skills, experiences, or qualifications that are missing.

3. KEY STRENGTHS: What are the top 3 strengths in the resume that align well with this job? Explain why each is valuable for this position.

4. IMPROVEMENT SUGGESTIONS: Provide 2-3 specific suggestions for how the candidate could better position their resume for this job.

Be specific, constructive, and actionable in your feedback.
"""

# Chat Q&A prompt template
CHAT_TEMPLATE = """
You are an expert resume coach helping a job seeker understand how to improve their application.

Resume:
---
{resume}
---

Job Description:
---
{job_description}
---

Previous Analysis:
---
{analysis}
---

Chat History:
---
{chat_history}
---

The user has asked the following question:
{question}

Provide a helpful, specific, and actionable response based on the resume and job description context. Keep your answer focused on helping them improve their job application.
""" 