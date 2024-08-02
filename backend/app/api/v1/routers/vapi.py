import json
import io
import sys
import requests

from fastapi import Request, APIRouter
from app.core.log import logger

from app.core.config import settings

router = r = APIRouter()

sample_assistant_overrides = {
    "variableValues": {
        "jobDescription": """At Groq. We believe in an AI economy powered by human agency. We envision a world where AI is accessible to all, a world that demands processing power that is better, faster, and more affordable than is available today. AI applications are currently constrained by the limitations of the Graphics Processing Unit (GPU), a technology originally developed for the gaming market and soon to become the weakest link in the AI economy.

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

At Groq: Our goal is to hire and promote an exceptional workforce as diverse as the global populations we serve. Groq is an equal opportunity employer committed to diversity, inclusion, and belonging in all aspects of our organization. We value and celebrate diversity in thought, beliefs, talent, expression, and backgrounds. We know that our individual differences make us better.""",
        "jobName": "Software Engineer, Developer Experience",
        "companyName": "Groq",
        "questionBank": [ { "question": "Can you describe a time when you optimized the performance of a system or application? What was your approach, and what was the outcome?", "keyPoints": [ "Identified performance bottlenecks", "Implemented optimization techniques", "Measured and quantified improvements", "Collaborated with team members" ], "skillsToDemo": [ "System Optimization", "Problem-solving", "Attention to Detail" ], "scoring": { "1": "Poor: Unable to provide an example of performance optimization or demonstrates a lack of understanding of the concept.", "2": "Below Average: Provides a vague or irrelevant example of performance optimization without clear results.", "3": "Average: Describes a basic performance optimization scenario but lacks specific details or significant measurable outcomes.", "4": "Good: Provides a clear example of performance optimization with some measurable results, but may lack depth in some areas.", "5": "Excellent: Demonstrates deep understanding of performance optimization techniques, provides specific examples with measurable outcomes, and shows collaborative problem-solving skills." } }, { "question": "Tell me about a time when you wrote code for a complex API. How did you ensure its simplicity and effectiveness?", "keyPoints": [ "Understood API requirements", "Designed clear and intuitive endpoints", "Implemented error handling and informative messages", "Documented the API thoroughly" ], "skillsToDemo": [ "Software Development", "API Design", "Attention to Detail" ], "scoring": { "1": "Poor: Unable to provide an example of API development or shows a lack of understanding of API design principles.", "2": "Below Average: Gives a vague description of API development without addressing simplicity or effectiveness.", "3": "Average: Provides a basic example of API development but lacks emphasis on simplicity or effectiveness.", "4": "Good: Describes a well-designed API with consideration for simplicity, but may lack depth in one area (e.g., error handling or documentation).", "5": "Excellent: Demonstrates strong API design principles, emphasizes simplicity and effectiveness, provides specific examples of error handling and documentation." } }, { "question": "Can you describe a time when you received and acted on feedback from colleagues or customers? How did you incorporate their suggestions into your work?", "keyPoints": [ "Received feedback from colleagues or customers", "Acted on feedback by making changes", "Incorporated feedback into future work", "Communicated changes to the team" ], "skillsToDemo": [ "Communication", "Collaboration", "Emotional Intelligence" ], "scoring": { "1": "Poor: Unable to provide an example of receiving and responding to feedback or shows a lack of understanding of its importance.", "2": "Below Average: Gives a vague description of receipt and response to feedback without clear implementation or improvement.", "3": "Average: Describes a basic scenario of receiving and responding to feedback but lacks specific implementation or follow-through.", "4": "Good: Provides a clear example of incorporating feedback and making improvements, but may lack significant communication or process changes.", "5": "Excellent: Demonstrates strong ability to incorporate feedback, communicate changes clearly, and improve processes." } }, { "question": "Can you describe a time when you advocated for a solution that required making a trade-off between competing priorities?", "keyPoints": [ "Identified conflicting priorities", "Advocated for a solution that addressed multiple priorities", "Communicated and justified the trade-off", "Implemented the solution" ], "skillsToDemo": [ "Decision-making", "Communication", "Problem-solving" ], "scoring": { "1": "Poor: Unable to provide an example of advocating for a trade-off or shows a lack of understanding of its importance.", "2": "Below Average: Gives a vague description of trade-off without clear details or justifications.", "3": "Average: Describes a basic scenario of making a trade-off between competing priorities but lacks specific details or justifications.", "4": "Good: Provides a clear example of advocating for a solution and communicating the trade-off, but may lack complete justification.", "5": "Excellent: Demonstrates strong decision-making, communication, and problem-solving skills, with clear justification for the trade-off." } }, { "question": "Can you describe a time when you took initiative to solve a complex problem or implement a new idea?", "keyPoints": [ "Identified a problem or opportunity", "Developed a plan to address the problem or implement the idea", "Implemented the solution", "Communicated results to the team" ], "skillsToDemo": [ "Initiative", "Problem-solving", "Communication" ], "scoring": { "1": "Poor: Unable to provide an example of taking initiative or shows a lack of understanding of its importance.", "2": "Below Average: Gives a vague description of taking initiative without clear details or results.", "3": "Average: Describes a basic scenario of taking initiative but lacks specific details or results.", "4": "Good: Provides a clear example of taking initiative and implementing a solution, but may lack significant communication or results.", "5": "Excellent: Demonstrates strong initiative, problem-solving, and communication skills, with clear results and follow-through." } }, { "question": "Can you describe a time when you received and successfully implemented feedback from a mentor or manager?", "keyPoints": [ "Received feedback from a mentor or manager", "Acted on feedback by making changes", "Implemented feedback into future work", "Communicated changes to the team" ], "skillsToDemo": [ "Emotional Intelligence", "Collaboration", "Communication" ], "scoring": { "1": "Poor: Unable to provide an example of receiving and responding to feedback or shows a lack of understanding of its importance.", "2": "Below Average: Gives a vague description of receipt and response to feedback without clear implementation or improvement.", "3": "Average: Describes a basic scenario of receiving and responding to feedback but lacks specific implementation or follow-through.", "4": "Good: Provides a clear example of incorporating feedback and making improvements, but may lack significant communication or process changes.", "5": "Excellent: Demonstrates strong ability to incorporate feedback, communicate changes clearly, and improve processes." } }, { "question": "Can you describe a time when you contributed to a team effort to develop and launch a new product or feature?", "keyPoints": [ "Participated in team planning and coordination", "Contributed to the development of the product or feature", "Assisted with testing and validation", "Communicated with stakeholders" ], "skillsToDemo": [ "Collaboration", "Communication", "Problem-solving" ], "scoring": { "1": "Poor: Unable to provide an example of participating in a team effort or shows a lack of understanding of its importance.", "2": "Below Average: Gives a vague description of participating in a team effort without clear details or results.", "3": "Average: Describes a basic scenario of participating in a team effort but lacks specific details or results.", "4": "Good: Provides a clear example of contributing to a team effort and implementing the product or feature, but may lack significant communication or results.", "5": "Excellent: Demonstrates strong collaboration, communication, and problem-solving skills, with clear results and follow-through." } } ]
    }
}

@r.post("/start")
async def start_vapi(request: Request):
    vapi = request.app.state.vapi

    # Get the assistant overrides from the request body
    # TODO: fix this later
    assistant_overrides = await request.json()
    # assistant_overrides = sample_assistant_overrides
    assistant_overrides["variableValues"]["questionBank"] = json.dumps(assistant_overrides["variableValues"]["questionBank"])
    # Redirect stdout to capture the output
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()

    try:
        logger.info(assistant_overrides)
        vapi.start(assistant_id=settings.VAPI_ASSISTANT_ID, assistant_overrides=assistant_overrides)
        output = buffer.getvalue()

        # Extract call_id from the output
        call_id = None
        for line in output.split("\n"):
            if line.startswith("Joining call..."):
                call_id = line.split()[-1]
                break

        return {
            "message": "Vapi started successfully",
            "call_id": call_id,
            "output": output,
        }
    finally:
        # Restore stdout
        sys.stdout = old_stdout


@r.post("/stop")
def stop_vapi(request: Request):
    vapi = request.app.state.vapi
    vapi.stop()
    return {"message": "Vapi stopped successfully"}


@r.post("/fetch_transcript")
async def fetch_transcript(request: Request):
    call_id = request.query_params.get("call_id")
    url = f"https://api.vapi.ai/call/{call_id}"
    # private_api_key = "72350235-1452-427e-b987-b7b96766a777"
    headers = {"Authorization": f"Bearer {settings.VAPI_API_KEY_PRIVATE}"}
    logger.info(f"Fetching transcript for call_id: {call_id}")
    try:
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Transcript data: {data}")
        transcript = data.get("transcript", "")
        return {"transcript": transcript}
    except Exception as e:
        return {"error": str(e)}

@r.get("/info")
def info():
    # try:
    import pyaudio
    pa = pyaudio.PyAudio()
    return {
        "get_default_output_device_info": pa.get_default_output_device_info(),
        "file": pa.__file__
    }
    # except Exception as e:
    #     return {"error": str(e)}
    # finally:
    #     pa.terminate()
