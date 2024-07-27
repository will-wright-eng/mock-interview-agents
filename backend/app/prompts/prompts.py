job_description_prompt = {
    "system": """You are an AI mock interviewer designed to help job seekers practice behavioral interviews. Your task is to analyze a job description, generate relevant interview questions, provide grading criteria for each question, and create an overall grading rubric for the interview.

First, carefully read and analyze the given job description. Based on the job description, follow these steps:

1. Generate a list of 5-7 behavioral interview questions that are relevant to the position and the skills/qualities mentioned in the job description. Each question should assess a different aspect of the candidate's experience, skills, or personality traits.

2. For each question, create a grading criteria that includes:
   a) Key points the candidate should cover in their answer
   b) Skills or qualities the answer should demonstrate
   c) A scoring system (e.g., 1-5 scale) with descriptions for each score level

3. Develop an overall rubric for the entire interview that includes:
   a) Criteria for evaluating the candidate's overall performance
   b) Weightings for different aspects of the interview (e.g., content of answers, communication skills, etc.)
   c) A scoring system to determine the final grade (e.g., A, B, C, D, or F)

Each question should have the following data:
- Question content
- Key points 
- Skills quality to demonstrate
  - Scoring:
     5 - Excellent: [Description]
     4 - Good: [Description]
     3 - Average: [Description]
     2 - Below Average: [Description]
     1 - Poor: [Description]

Include an overall rubric for the interview as well:
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

Ensure that your questions, grading criteria, and overall rubric are tailored to the specific job description provided. Focus on assessing the key skills, experiences, and qualities mentioned in the job posting.
"""
}

report_card_prompt = {
    "system": """

You are an AI assistant tasked with grading a mock interview based on a provided transcript, question bank, answer rubrics, and overall rubrics. Your goal is to provide a comprehensive report card that will help the candidate improve their interview skills. Follow these instructions carefully:

1. First, you will be given the interview transcript. Read it carefully to understand the flow of the conversation and the candidate's responses.

2. Next, you will be provided with the question bank. This contains the questions that were asked during the interview. The interview typically begins with introductions and some biographical information. You should also grade the candidate on these responses.

3. You will also receive answer rubrics for each question. These rubrics provide criteria for evaluating the candidate's responses.

4. Finally, you will be given overall rubrics to assess the candidate's general performance throughout the interview.

5. Analyze the transcript:
   a. Identify each question from the question bank in the transcript.
   b. Locate the candidate's response to each question.
   c. Note any additional relevant information, such as the candidate's demeanor, confidence, or communication style.

6. Grade individual questions:
   a. For each question, compare the candidate's response to the corresponding answer rubric.
   b. Provide a brief justification for your assessment, highlighting strengths and areas for improvement.
   c. Assign a score based on the rubric criteria.
   d. Use a "Question assessment:" prefix before your evaluation for each question.

7. Overall assessment:
   a. Review the overall rubrics and assess the candidate's performance across the entire interview.
   b. Consider factors such as communication skills, professionalism, and general interview etiquette.
   c. Provide a summary of the candidate's strengths and areas for improvement.
   d. Assign an overall score based on the rubric criteria.
   e. Use an "Overall assessment:" prefix to enclose your overall evaluation.

8. Format the final report card:
   a. Begin with an introduction summarizing the purpose of the report card.
   b. Present the individual question assessments in the order they appeared in the interview.
   c. Follow with the overall assessment.
   d. Conclude with specific recommendations for improvement.
   e. Prefix the entire report card with "Report card:".

Here's an example of how your report card should be structured:

Report card:
Introduction:
This report card evaluates your performance in the mock interview. It provides feedback on individual questions and an overall assessment to help you improve your interview skills.

Question assessment:
Question: [Insert question here]
Justification: [Provide brief justification for the assessment]
Score: [Insert score]

[Repeat for each question]

Overall assessment:
Overall Performance:
Strengths: [List key strengths]
Areas for Improvement: [List areas that need improvement]
Overall Score: [Insert overall score]

Recommendations:
To improve your interview performance, consider the following:
1. [Specific recommendation]
2. [Specific recommendation]
3. [Specific recommendation]

Remember to be objective, constructive, and specific in your feedback. Your goal is to help the candidate improve their interview skills.
"""
}

sample_job_description = """
Job description:
Software Engineer, Developer Experience
Palo Alto, CA

At Groq. We believe in an AI economy powered by human agency. We envision a world where AI is accessible to all, a world that demands processing power that is better, faster, and more affordable than is available today. AI applications are currently constrained by the limitations of the Graphics Processing Unit (GPU), a technology originally developed for the gaming market and soon to become the weakest link in the AI economy.

Enter Groq's LPU™ Inference Engine. Specifically engineered for the demands of large language models (LLMs), the Language Processing Unit outpaces the GPU in speed, power, efficiency, and cost-effectiveness. The quickest way to understand the opportunity is to watch the following talk – groq.link/scspdemo.

Why join Groq? AI will change humanity forever, and we believe preservation of human agency and self determination is only possible if AI is made affordably and universally accessible. Groq’s LPUs will power AI from an early stage, and you will get to leave your fingerprint on civilization.

Software Engineer, Developer Experience

Mission: ship code daily to improve the suite of APIs that >200k developers use to build fast AI applications.

Responsibilities & opportunities in this role:

Software Development: Write simple, concise, high-performance code for both our apis written in Golang and our webapp in Next.js.
System Optimization: Performance is everything at Groq. We have dedicated performance teams, but all engineers need to focus on where the milliseconds are spent.
Attention to Detail: Uphold a high standard for code quality and user experience. While building great new functionality, also take pride in making error messages clearer and more actionable.
Sample Projects
Function Calling and Tool Use - Add tool use capabilities to our inference apis and add support for new models we bring on board
Self Serve Billing - Build out the ability for developers to create accounts and sign up to our self serve billing tier
Batch Jobs - Build out a mechanism for developers to submit batch jobs that run inference workloads asynchronously when capacity isn’t full.
Ideal candidates have/are:

Curiosity: Genuine interest in AI and how Language models are enabling new use cases across a variety of industries
Self-Driven: Ability to see projects through end-to-end independently.
Bias to Action: Make decisions and ship code. You shouldn’t like meetings.
Attributes of a Groqster:

Humility - Egos are checked at the door
Collaborative & Team Savvy - We make up the smartest person in the room, together
Growth & Giver Mindset - Learn it all versus know it all, we share knowledge generously
Curious & Innovative - Take a creative approach to projects, problems, and design
Passion, Grit, & Boldness - no limit thinking, fueling informed risk taking
If this sounds like you, we’d love to hear from you!

Compensation: At Groq, a competitive base salary is part of our comprehensive compensation package, which includes equity and benefits. For this role, the base salary range is $145,400 to $276,500, determined by your skills, qualifications, experience and internal benchmarks.

Location: Groq is a geo-agnostic company, meaning you work where you are. Exceptional candidates will thrive in asynchronous partnerships and remote collaboration methods. Some roles may require being located near our primary sites, as indicated in the job description.  

At Groq: Our goal is to hire and promote an exceptional workforce as diverse as the global populations we serve. Groq is an equal opportunity employer committed to diversity, inclusion, and belonging in all aspects of our organization. We value and celebrate diversity in thought, beliefs, talent, expression, and backgrounds. We know that our individual differences make us better.
"""

sample_transcript = """
AI: Hi. Thanks for taking the time to meet with me today. How are you doing?
User: Doing well. How are you?
AI: I'm doing great. Thank you for asking. Let's start by having you tell me a bit about yourself, and your background. What led you to apply for a role at Open AI? And what makes you interested? This particular position?
User: Um, well, I think OpenAI is, like, a super cool, really popular company. And it's like the top AI company around. So yeah, I just really wanna work at, like, the top company.
AI: That's great to hear.
User: To hear.
AI: Working yes. OpenAI is definitely at the cutting edge of AI research. Deployment. Now I'd like to know more about your background and experience. Could you tell me about your relevant engineering experience and how it aligns with the requirements, of the role at Open
User: No. No. No. No. Because before so this is really cool. Before, uh, how do I Stop.
AI: No worries.
User: I was gonna say you should do you should alternate between really good answers and really bad answers.
"""

sample_question_bank_and_rubric = """
Question bank:
1. Can you describe a project you worked on where you had to optimize the performance of a complex system? What steps did you take to identify bottlenecks, and how did you measure the impact of your changes?

Grading Criteria:
- Key points: Description of the project, identification of bottlenecks, steps taken to optimize performance, measurement of impact
- Skills/qualities to demonstrate: Problem-solving, analytical thinking, attention to detail, ability to measure and evaluate performance
- Scoring:
  5 - Excellent: Provides a clear, concise description of the project and optimization process, including metrics to measure impact
  4 - Good: Provides a good description of the project, but lacks detail on optimization steps or metrics
  3 - Average: Provides a general overview of the project, but lacks specific examples or metrics
  2 - Below Average: Struggles to describe the project or optimization process, lacks any metrics or measurement of impact
  1 - Poor: Fails to describe the project or optimization process

2. Tell me about a time when you had to work on a team to develop a new feature or API. What was your role in the project, and how did you contribute to its success?

Grading Criteria:
- Key points: Description of the project, role in the project, contributions to success
- Skills/qualities to demonstrate: Teamwork, collaboration, communication, ability to contribute to a team effort
- Scoring:
  5 - Excellent: Provides a clear, concise description of the project and their role, including specific examples of contributions to success
  4 - Good: Provides a good description of the project and their role, but lacks specific examples of contributions
  3 - Average: Provides a general overview of the project, but lacks detail on their role or contributions
  2 - Below Average: Struggles to describe the project or their role, lacks any examples of contributions
  1 - Poor: Fails to describe the project or their role

3. How do you approach debugging complex issues in your code? Can you walk me through your thought process and the steps you take to identify and fix the issue?

Grading Criteria:
- Key points: Description of debugging process, thought process, steps taken to identify and fix the issue
- Skills/qualities to demonstrate: Problem-solving, analytical thinking, attention to detail, ability to debug complex issues
- Scoring:
  5 - Excellent: Provides a clear, concise description of their debugging process, including specific examples of thought process and steps taken
  4 - Good: Provides a good description of their debugging process, but lacks specific examples or detail
  3 - Average: Provides a general overview of their debugging process, but lacks specific examples or detail
  2 - Below Average: Struggles to describe their debugging process, lacks any specific examples or detail
  1 - Poor: Fails to describe their debugging process

4. Can you describe a project or feature you worked on that required you to balance competing priorities, such as performance, security, and user experience? How did you approach this project, and what was the outcome?

Grading Criteria:
- Key points: Description of the project, competing priorities, approach to balancing priorities, outcome
- Skills/qualities to demonstrate: Problem-solving, analytical thinking, ability to balance competing priorities, attention to detail
- Scoring:
  5 - Excellent: Provides a clear, concise description of the project and their approach, including specific examples of balancing competing priorities
  4 - Good: Provides a good description of the project and their approach, but lacks specific examples or detail
  3 - Average: Provides a general overview of the project, but lacks detail on their approach or outcome
  2 - Below Average: Struggles to describe the project or their approach, lacks any specific examples or detail
  1 - Poor: Fails to describe the project or their approach

5. Tell me about a time when you had to make a decision quickly, without having all the information. What was the decision, and how did you approach making it?

Grading Criteria:
- Key points: Description of the situation, decision made, approach to making the decision
- Skills/qualities to demonstrate: Decision-making, ability to act quickly, analytical thinking
- Scoring:
  5 - Excellent: Provides a clear, concise description of the situation and decision made, including specific examples of their thought process
  4 - Good: Provides a good description of the situation and decision made, but lacks specific examples or detail
  3 - Average: Provides a general overview of the situation, but lacks detail on their approach or thought process
  2 - Below Average: Struggles to describe the situation or decision made, lacks any specific examples
"""

sample_overall_rubric = """
**Overall Rubric:**

Evaluation Criteria:

* Technical expertise: 30%
	+ Weighting: 30% of overall score
	+ Description: Ability to demonstrate technical skills and knowledge in software development, AI/NLP, and problem-solving.
* Collaboration and communication: 20%
	+ Weighting: 20% of overall score
	+ Description: Ability to work effectively with teams, communicate technical information, and resolve conflicts.
* Problem-solving and adaptability: 25%
	+ Weighting: 25% of overall score
	+ Description: Ability to approach complex problems, adapt to new information, and make data-driven decisions.
* Soft skills: 25%
	+ Weighting: 25% of overall score
	+ Description: Ability to demonstrate emotional intelligence, humility, and a growth mindset.

Final Grading Scale:

* A (90-100%): Exceptional candidate with outstanding technical expertise, strong collaboration and communication skills, and excellent problem-solving abilities. Demonstrates a high level of emotional intelligence, humility, and growth mindset.
* B (80-89%): Strong candidate with good technical expertise, strong collaboration and communication skills, and good problem-solving abilities. May have some areas for improvement in emotional intelligence, humility, or growth mindset.
* C (70-79%): Satisfactory candidate with decent technical expertise, adequate collaboration and communication skills, and fair problem-solving abilities. May lack some technical knowledge or struggle with collaboration and communication.
* D (60-69%): Marginal candidate with limited technical expertise, weak collaboration and communication skills, and poor problem-solving abilities. May require additional training or support to succeed.
* F (0-59%): Unsatisfactory candidate with poor technical expertise, weak collaboration and communication skills, and limited problem-solving abilities. May not be a good fit for the role.
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
