const sampleData = {
    company: "Groq",
    jobTitle: "Software Engineer, Developer Experience",
    jobDescription: `At Groq. We believe in an AI economy powered by human agency. We envision a world where AI is accessible to all, a world that demands processing power that is better, faster, and more affordable than is available today. AI applications are currently constrained by the limitations of the Graphics Processing Unit (GPU), a technology originally developed for the gaming market and soon to become the weakest link in the AI economy.

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

At Groq: Our goal is to hire and promote an exceptional workforce as diverse as the global populations we serve. Groq is an equal opportunity employer committed to diversity, inclusion, and belonging in all aspects of our organization. We value and celebrate diversity in thought, beliefs, talent, expression, and backgrounds. We know that our individual differences make us better.`
}
export default sampleData;

const sampleReportCard = {
    questionAssessment: [
      {
        question:
          "Can you tell me a little bit about your background and experience as a software engineer?",
        justification:
          "You provided a brief overview of your experience, including your time at Amazon and Google. However, you could have elaborated more on your specific accomplishments and skills.",
        score: 4,
        scoreDescription: "Good",
      },
      {
        question:
          "Can you tell me about a specific project or feature you worked on that you're particularly proud of?",
        justification:
          "You provided a good example of a project you worked on at Google, including the design process and launch. However, you could have elaborated more on the technical details and challenges you faced.",
        score: 4,
        scoreDescription: "Good",
      },
      {
        question:
          "Can you describe a project you worked on where you had to optimize the performance of a complex system? What steps did you take to identify bottlenecks? And how did you measure the impact of your changes?",
        justification:
          "You provided a clear and concise description of a project you worked on, including the steps you took to optimize performance and measure impact. You demonstrated good problem-solving and analytical thinking skills.",
        score: 5,
        scoreDescription: "Excellent",
      },
      {
        question:
          "Tell me about a time when you had to work on a team to develop a new feature or API. What was your role in the project, and how did you contribute to its success?",
        justification:
          "You struggled to provide a clear description of your role in the project and your contributions to its success. You could have elaborated more on your specific responsibilities and how you worked with the team.",
        score: 2,
        scoreDescription: "Below Average",
      },
      {
        question: "Is this role remote or in person?",
        justification:
          "This was not a technical question, but rather a question about the role. You provided a brief answer, but could have elaborated more on your preferences and expectations.",
        score: "N/A",
      },
    ],
    overallAssessment: {
      technicalExpertise: {
        score: 22,
        outOf: 30,
        percentage: 73,
        comments: [
          "You demonstrated good technical expertise in your answers, particularly in the question about optimizing the performance of a complex system.",
          "However, you struggled to provide detailed technical answers in other questions.",
        ],
      },
      collaborationAndCommunication: {
        score: 16,
        outOf: 20,
        percentage: 80,
        comments: [
          "You demonstrated good communication skills in your answers, but struggled to provide clear descriptions of your role in team projects.",
          "You could have elaborated more on your approach to collaboration and teamwork.",
        ],
      },
      problemSolvingAndAdaptability: {
        score: 20,
        outOf: 25,
        percentage: 80,
        comments: [
          "You demonstrated good problem-solving skills in your answers, particularly in the question about optimizing the performance of a complex system.",
          "However, you could have elaborated more on your approach to problem-solving and adaptability.",
        ],
      },
      softSkills: {
        score: 18,
        outOf: 25,
        percentage: 72,
        comments: [
          "You demonstrated good soft skills in your answers, such as humility and enthusiasm for learning.",
          "However, you could have elaborated more on your emotional intelligence and growth mindset.",
        ],
      },
    },
    overallScore: 76,
    grade: "B",
    gradeDescription:
      "Satisfactory candidate with good technical expertise, strong collaboration and communication skills, but some areas for improvement",
    recommendations: [
      "Practice providing clear and concise answers to technical questions.",
      "Elaborate more on your specific accomplishments and skills in your answers.",
      "Prepare examples of your teamwork and collaboration experiences.",
      "Practice demonstrating your emotional intelligence and growth mindset in your answers.",
    ],
  };
  