import { useState, useEffect } from "react";
import Layout from "../components/Layout";
import MdDisplay from "../components/MdDisplay";
import sampleData from "./sampleData";

const sampleReportCard = `Report card:

Introduction:
This report card evaluates your performance in the mock interview for the Software Engineer, Developer Experience position at Groq. It provides feedback on individual questions and an overall assessment to help you improve your interview skills.

Question assessment:
Question: Can you describe a time when you had to optimize the performance of a system or application? What was your approach, and what was the outcome?
The candidate failed to provide a specific example or details about their approach to system optimization. They mentioned working at large companies and smaller startups, but did not provide any relevant information about optimizing performance.
Score: 2 (Below Average)

Question: Tell me about a time when you had to write code for a complex API. How did you ensure its simplicity and effectiveness?
The candidate provided a vague description of API development without addressing simplicity or effectiveness. They mentioned working with Golang and Next.js, but did not provide any specific examples or details about API design.
Score: 2 (Below Average)

Question: How do you approach coding in a collaborative environment? Can you give an example of a successful project you worked on with a team where you received feedback and made adjustments?
The candidate mentioned a team project, but lacked concrete examples or specific details about collaborative activities. They showed some willingness to receive feedback, but did not provide any examples of adjustments made.
Score: 3 (Average)

Question: Tell me about a time when you identified a problem or inefficiency in a project or process and suggested a solution. What was the outcome?
The candidate mentioned a problem or inefficiency, but lacked specific details or results. They suggested a solution, but did not communicate effectively with team members or document the impact of the solution.
Score: 3 (Average)

Question: Can you walk me through how you approach learning and staying current with new technologies and methodologies in software development?
The candidate mentioned a desire to learn new technologies, but lacked concrete examples or results. They did not provide any specific details about self-directed learning or exploring new tools and techniques.
Score: 3 (Average)

Question: Tell me about a time when you had to handle a difficult situation or customer complaint. How did you resolve it?
The candidate failed to describe any experience handling difficult situations. They did not show empathy or understanding, and did not provide effective solutions or communication.
Score: 2 (Below Average)

Question: Can you describe your experience with Golang and Next.js, and how you approach using these technologies in software development?
The candidate mentioned experience with Golang and Next.js, but did not provide specific examples or details about best practices and principles.
Score: 3 (Average)

Overall assessment:
Overall Performance:
Strengths: The candidate has 10 years of experience in software engineering, and has worked at both large companies and smaller startups.
Areas for Improvement: The candidate needs to provide more specific examples and details about their experience in system optimization, API development, collaboration, and problem-solving. They also need to demonstrate a stronger understanding of Groq's mission and culture.
Overall Score: 67% (B- grade)

Recommendations:
To improve your interview performance, consider the following:

1. Provide more specific examples and details about your experience in system optimization, API development, and collaboration.
2. Demonstrate a stronger understanding of Groq's mission and culture, and be prepared to discuss how your skills and experience align with the company's values.
3. Practice answering behavioral interview questions in a more concise and specific way.
4. Emphasize your attention to detail and ability to work effectively in a remote environment.
5. Show enthusiasm for learning new technologies and approaches, and provide specific examples of self-directed learning and professional development activities.

Note: Based on the final grading scale, this candidate would receive a B- grade, meaning they are a strong candidate who demonstrates proficiency in most areas but may need development in some areas.`

export default function Home() {
  const [company, setCompany] = useState("");
  const [jobTitle, setJobTitle] = useState("");
  const [jobDescription, setJobDescription] = useState("");
  const [questions, setQuestions] = useState("");
  const [overallRubric, setOverallRubric] = useState("");
  const [isReadyForInterview, setIsReadyForInterview] = useState(false);
  const [conversationState, setConversationState] = useState("inactive");
  const [callId, setCallId] = useState("");
  const [reportCard, setReportCard] = useState(sampleReportCard);
  const [interviewFinished, setInterviewFinished] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [transcript, setTranscript] = useState("");

  const useTemplate = () => {
    console.log({ sampleData });
    setCompany(sampleData.company);
    setJobTitle(sampleData.jobTitle);
    setJobDescription(sampleData.jobDescription);
    console.log({ company, jobTitle, jobDescription });
  };

  useEffect(() => {
    console.log("isReadyForInterview:", isReadyForInterview);
    console.log("questions:", questions);
  }, [isReadyForInterview, questions]);

  const generateQuestionsAndRubric = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/v1/doc_gen/generate_questions_and_rubric",
        {
          method: "POST",
          headers: {
            accept: "application/json",
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            jobTitle: jobTitle,
            company: company,
            jobDescription: jobDescription,
          }),
        }
      );

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log("Received data:", data); // Log the received data

      if (data) {
        // Assuming the questions are in the 'cv' field
        setQuestions(data.interviewQuestions);
        setOverallRubric(data.overallRubric);
        setIsReadyForInterview(true);
        console.log("Questions set and interview ready"); // Add this log
      } else {
        console.error("No questions received in the response");
        setIsReadyForInterview(false); // Ensure this is set to false if no questions are received
      }
    } catch (error) {
      console.error("Error generating questions and rubric:", error);
      setIsReadyForInterview(false); // Ensure this is set to false on error
    }
  };

  const handleSubmit = async () => {
    setIsSubmitting(true);
    try {
      await generateQuestionsAndRubric();
    } catch (error) {
      console.error("Error in the submission process:", error);
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleConversation = async () => {
    if (conversationState === "inactive") {
      await startInterview();
    } else {
      await stopInterview();
    }
  };

  const startInterview = async () => {
    setConversationState("active");
    setInterviewFinished(false);
    try {
      console.log({ jobDescription, jobTitle, company, questions });
      const response = await fetch("http://127.0.0.1:8000/api/v1/vapi/start", {
        method: "POST",
        headers: {
          accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          variableValues: {
            jobDescription: jobDescription,
            jobTitle: jobTitle,
            companyName: company,
            questionBank: questions,
          },
        }),
      });
      const data = await response.json();
      console.log("Conversation started:", data);
      if (data.call_id) {
        setCallId(data.call_id);
      }
    } catch (error) {
      console.error("Error starting conversation:", error);
      setConversationState("inactive");
    }
  };

  const stopInterview = async () => {
    setConversationState("inactive");
    try {
      const response = await fetch("http://127.0.0.1:8000/api/v1/vapi/stop", {
        method: "POST",
        headers: {
          accept: "application/json",
          "Content-Type": "application/json",
        },
      });
      const data = await response.json();
      console.log("Conversation stopped:", data);
      setInterviewFinished(true);
    } catch (error) {
      console.error("Error stopping conversation:", error);
    }
  };

  const restartInterview = async () => {
    setCallId("");
    setReportCard("");
    setInterviewFinished(false);
    await startInterview();
  };

  const generateReportCard = async () => {
    try {
      // Fetch transcript
      console.log({callId})
      const transcriptResponse = await fetch(
        `http://127.0.0.1:8000/api/v1/vapi/fetch_transcript?call_id=${callId}`,
        {
          method: "POST",
          headers: {
            accept: "application/json",
          },
        }
      );
      const transcriptData = await transcriptResponse.json();
      setTranscript(transcriptData.transcript);
      console.log({transcript})

      // Generate report card
      console.log({jobDescription, jobTitle, company, questions, overallRubric, transcript})
      const reportCardResponse = await fetch(
        "http://127.0.0.1:8000/api/v1/doc_gen/generate_report_card",
        {
          method: "POST",
          headers: {
            accept: "application/json",
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            job_description: jobDescription,
            job_title: jobTitle,
            company: company,
            question_bank: questions,
            transcript: transcript,
            overall_rubric: overallRubric,
          }),
        }
      );
      const reportCardData = await reportCardResponse.json();
      console.log({reportCardData})
      setReportCard(reportCardData.report_card);
    } catch (error) {
      console.error("Error generating report card:", error);
    }
  };

  return (
    <Layout>
      <div className="hero min-h-screen bg-base-200">
        <div className="hero-content text-center">
          <div className="max-w-md">
            <h1 className="text-5xl font-bold">Welcome to Dream Job! 🌟</h1>
            <p className="py-6">
              Prepare for your dream job with our mock interview platform.
              Practice, improve, and ace your interviews.
            </p>
            <div>
              <button className="btn btn-info mb-4" onClick={useTemplate}>
                Use Template
              </button>
            </div>
            <input
              type="text"
              placeholder="Company"
              value={company}
              onChange={(e) => setCompany(e.target.value)}
              className="input input-bordered w-full max-w-xs mb-4"
            />
            <input
              type="text"
              placeholder="Job Title"
              value={jobTitle}
              onChange={(e) => setJobTitle(e.target.value)}
              className="input input-bordered w-full max-w-xs mb-4"
            />
            <textarea
              placeholder="Job Description"
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
              className="textarea textarea-bordered w-full max-w-xs mb-4"
              rows="10"
            />
            <div className="flex justify-center">
              <button
                className="btn btn-primary"
                onClick={handleSubmit}
                disabled={isSubmitting}
              >
                {isSubmitting ? "Submitting..." : "Submit"}
              </button>
            </div>
            {isReadyForInterview && !interviewFinished && !isSubmitting && (
              <button
                className="btn btn-secondary mt-4"
                onClick={handleConversation}
              >
                {conversationState === "inactive"
                  ? "Start Interview"
                  : "Stop Interview"}
              </button>
            )}
            {interviewFinished && !isSubmitting && (
              <>
                <button
                  className="btn btn-accent mt-4 mr-2"
                  onClick={generateReportCard}
                >
                  Generate Report Card
                </button>
                <button
                  className="btn btn-secondary mt-4"
                  onClick={restartInterview}
                >
                  Restart Interview
                </button>
              </>
            )}

            {questions && !isSubmitting && (
              <MdDisplay
                content={JSON.stringify(questions, null, 2)}
                title="Generated Questions"
              />
            )}
            {overallRubric && !isSubmitting && (
              <MdDisplay
                content={JSON.stringify(overallRubric, null, 2)}
                title="Overall Rubric"
              />
            )}
            {reportCard && !isSubmitting && (
              <MdDisplay
                content={reportCard}
                title="Report Card"
              />
            )}
          </div>
        </div>
      </div>
    </Layout>
  );
}
