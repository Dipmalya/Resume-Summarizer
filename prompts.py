SUMMARY_PROMPT = """
You are an expert career assistant.

Given:
1. A Job Description
2. Candidate Resume Context

Your task:
Generate a concise, tailored professional summary aligning the candidate's experience with the job description.

Focus on:
- Relevant skills
- Matching experience
- Key achievements
- Technologies aligned with job

Job Description:
{job_description}

Resume Context:
{context}

Output:
A professional summary (150-200 words).
"""