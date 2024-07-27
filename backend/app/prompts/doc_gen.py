rubric_gen_prompt = """this is a placeholder
"""

question_gen_prompt = """You are an AI mock interviewer designed to help job seekers practice behavioral interviews. Your task is to analyze a job description, generate relevant interview questions, provide grading criteria for each question, and create an overall rubric for the interview.

First, carefully read and analyze the following job description:

<job_description>
{{JOB_DESCRIPTION}}
</job_description>

Based on this job description, follow these steps:

1. Generate a list of 5-7 behavioral interview questions that are relevant to the position and the skills/qualities mentioned in the job description. Each question should assess a different aspect of the candidate's experience, skills, or personality traits.

2. For each question, create a grading criteria that includes:
   a) Key points the candidate should cover in their answer
   b) Skills or qualities the answer should demonstrate
   c) A scoring system (e.g., 1-5 scale) with descriptions for each score level

3. Develop an overall rubric for the entire interview that includes:
   a) Criteria for evaluating the candidate's overall performance
   b) Weightings for different aspects of the interview (e.g., content of answers, communication skills, etc.)
   c) A scoring system to determine the final grade (e.g., A, B, C, D, or F)

Present your output in the following format:

<interview_questions>
1. [Question 1]
   Grading Criteria:
   - Key points: [List key points]
   - Skills/qualities to demonstrate: [List skills/qualities]
   - Scoring:
     5 - Excellent: [Description]
     4 - Good: [Description]
     3 - Average: [Description]
     2 - Below Average: [Description]
     1 - Poor: [Description]

2. [Question 2]
   [Follow the same format as Question 1]

[Continue for all questions]
</interview_questions>

<overall_rubric>
1. Evaluation Criteria:
   a) [Criterion 1]: [Description and weighting]
   b) [Criterion 2]: [Description and weighting]
   [Continue for all criteria]

2. Final Grading Scale:
   A (90-100%): [Description]
   B (80-89%): [Description]
   C (70-79%): [Description]
   D (60-69%): [Description]
   F (0-59%): [Description]
</overall_rubric>

Ensure that your questions, grading criteria, and overall rubric are tailored to the specific job description provided. Focus on assessing the key skills, experiences, and qualities mentioned in the job posting.
"""

cv_gen_prompt = """Please generate a CV for the following job title:

<job_title>
{JOB_TITLE}
</job_title>

Here is an example of a CV:

Software Engineer, Full Stack
Applied AI Engineering - San Francisco

About the Team

We bring OpenAI's technology to the world through products like ChatGPT and the OpenAI API.

We seek to learn from deployment and distribute the benefits of AI, while ensuring that this powerful tool is used responsibly and safely. Safety is more important to us than unfettered growth.

About the Role

We are looking for a self-starter engineer who loves building new products in an iterative and fast-moving environment. In this role, you will be bringing our large language models to millions of users around the world. Our users include everyday enthusiasts as well as professionals for ChatGPT, and everyone from hobbyists to large enterprises for the OpenAI API — you'll interface directly with users to develop the features they want most! You will also collaborate closely with the research teams that created the core models and work with them on continual improvement. You will be a key part of the effort to push these technologies forward, and onto the next 100x users.

 In this role, you will:

Own the development of new customer-facing ChatGPT and OpenAI API features and product experiences end-to-end

Talk to users to understand their problems and design solutions to address them

Work with the research team to get relevant feedback and iterate on their latest models

Collaborate with a cross-functional team of engineers, researchers, product managers, designers, and operations folks to create cutting-edge products

Optimize applications for speed and scale

Your background looks something like:

5+ years of relevant engineering experience at tech and product-driven companies

Proficiency with JavaScript, React, and other web technologies

Proficiency with some backend language (we use Python)

Some experience with relational databases like Postgres/MySQL

Interest in AI/ML (direct experience not required)

Ability to move fast in an environment where things are sometimes loosely defined and may have competing priorities or deadlines

About OpenAI

OpenAI is an AI research and deployment company dedicated to ensuring that general-purpose artificial intelligence benefits all of humanity. We push the boundaries of the capabilities of AI systems and seek to safely deploy them to the world through our products. AI is an extremely powerful tool that must be created with safety and human needs at its core, and to achieve our mission, we must encompass and value the many different perspectives, voices, and experiences that form the full spectrum of humanity.

We are an equal opportunity employer and do not discriminate on the basis of race, religion, national origin, gender, sexual orientation, age, veteran status, disability or any other legally protected status.

For US Based Candidates: Pursuant to the San Francisco Fair Chance Ordinance, we will consider qualified applicants with arrest and conviction records.

We are committed to providing reasonable accommodations to applicants with disabilities, and requests can be made via this link.

OpenAI Global Applicant Privacy Policy

At OpenAI, we believe artificial intelligence has the potential to help people solve immense global challenges, and we want the upside of AI to be widely shared. Join us in shaping the future of technology.

Compensation

$160K – $385K
"""

