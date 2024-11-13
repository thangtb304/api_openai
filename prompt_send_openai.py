system_prompt_candidate = f"""
Let's think step by step and response in Vietnamese.
CV details might be out of order or incomplete.
Analyze the CV concerning the candidate's experience and career. From this, derive logical conclusions about their technical skills, experience, and soft skills.
The format for educational qualifications should be: Degree - School/University/Organization - GPA - Year of Graduation. It's acceptable if some details are missing.
Experience should include experienced time and job name field of work based on projects and experiences.
Ensure that technical skills are mentioned explicitly and are not broad categories.
Responsibilities can get information from projects and experiences of candidate.
All comments should use singular pronouns such as "he", "she", "the candidate", or the candidate's name.
"""

fn_candidate_analysis = [
    {
        "name": "AnalyzeCV",
        "description": "Analyze candidate resume to get information.",
        "parameters": {
            "type": "object",
            "properties": {
                "candidate_name": {
                    "type": "string",
                    "description": "Name of the candidate.",
                },
                "phone_number": {
                    "type": "string",
                    "description": "Phone number of the candidate.",
                },
                "email": {
                    "type": "string",
                    "description": "Email of the candidate. e.g., jackey@gmail.com, hinata@outlook.com",
                },
                "degree": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Educational qualifications. e.g., Bachelor's degree in Computer Science - FPT University - 2024",
                },
                "experience": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Summary of experiences in fields the candidate has worked in.",
                },
                "technical_skill": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Specific technical skills and proficiencies. e.g., Java, Python, Linux, SQL.",
                },
                "responsibility": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Summary of responsibilities held by the candidate. e.g., Developed a fitness application on Android using Room Database, RxJava 2, and Retrofit 2.",
                },
                "certificate": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Certificates or qualifications achieved. e.g., Advanced Data Analysis, Basic SQL.",
                },
                "soft_skill": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Soft skills inferred from the resume, especially language and leadership skills. e.g., Language skills, leadership, critical thinking, problem-solving.",
                },
                "comment": {
                    "type": "string",
                    "description": "A summary about the candidate, including strengths, special skills, and years of experience relevant to the position.",
                },
                "job_recommended": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Recommended jobs for the candidate. e.g., Fullstack Web Developer, Python Developer, AI Engineer, Data Analyst.",
                },
                "office": {
                    "type": "integer",
                    "description": "Years of experience in office skills. For example, 0, 1, 2, 3,...",
                },
                "sql": {
                    "type": "integer",
                    "description": "Years of experience with SQL. For example, 0, 1, 2, 3,...",
                },
            },
            "required": [
                "candidate_name",
                "phone_number",
                "email",
                "degree",
                "experience",
                "technical_skill",
                "responsibility",
                "certificate",
                "soft_skill",
                "comment",
                "job_recommended",
                "office",
                "sql",
            ],
        },
    }
]
