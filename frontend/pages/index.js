import { useState, useEffect } from "react";
import Layout from "../components/Layout";
import MdDisplay from "../components/MdDisplay";
import sampleData from "./sampleData";

function ReportCardDisplay({ reportCardJSON }) {
  function convertReportCardToMarkdown(reportCard) {
    let markdown = `\n\n`;
  
    if (reportCard.introduction) {
      markdown += `${reportCard.introduction}\n\n`;
    }
  
    markdown += `#### Question Assessment\n\n\n\n`;
    reportCard.questionAssessment.forEach((qa, index) => {
      markdown += `### **Question ${index + 1}: ${qa.question}**\n\n\n\n\n\n`;
      markdown += `**Justification:** ${qa.justification}\n\n`;
      markdown += `**Score:** ${qa.score}${qa.scoreDescription ? ` (${qa.scoreDescription})` : ''}\n\n`;
      markdown += `---\n\n`; // Add a horizontal line between questions
    });
    markdown += `## **Overall Assessment**\n\n`;

    // Dynamically handle overall assessment categories
    Object.entries(reportCard.overallAssessment).forEach(
      ([key, assessment]) => {
        const title = key
          .split(/(?=[A-Z])/)
          .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
          .join(" ");

        markdown += `### **${title}: ${assessment.score !== undefined ? `${assessment.score}/5` : ''}**\n\n`;

        if (Array.isArray(assessment.comments)) {
          assessment.comments.forEach((comment) => {
            markdown += `- ${comment}\n`;
          });
        } else if (typeof assessment.comments === "string") {
          markdown += `- ${assessment.comments}\n`;
        }

        markdown += "\n---\n\n"; // Add separator between categories
      }
    );

    if (reportCard.overallScore !== undefined) {
      markdown += `## **Overall Score: ${reportCard.overallScore}/5**\n\n`;
    }

    if (reportCard.summary !== undefined) {
      markdown += `## **Summary**\n\n${reportCard.summary}\n\n`;
    }

    if (
      Array.isArray(reportCard.recommendations) &&
      reportCard.recommendations.length > 0
    ) {
      markdown += `## **Recommendations**\n\n`;
      reportCard.recommendations.forEach((recommendation, index) => {
        markdown += `${index + 1}. ${recommendation}\n`;
      });
    }
    return markdown;
  }

  const markdownContent = reportCardJSON
    ? convertReportCardToMarkdown(reportCardJSON)
    : "";

    return (
      <div className="w-full max-w-2xl mx-auto">
        <MdDisplay content={markdownContent} title="Report Card" />
      </div>
    );
  }

export default function Home() {
  const [company, setCompany] = useState("");
  const [jobTitle, setJobTitle] = useState("");
  const [jobDescription, setJobDescription] = useState("");
  const [questions, setQuestions] = useState("");
  const [overallRubric, setOverallRubric] = useState("");
  const [isReadyForInterview, setIsReadyForInterview] = useState(false);
  const [conversationState, setConversationState] = useState("inactive");
  const [callId, setCallId] = useState("");
  const [reportCard, setReportCard] = useState("");
  const [interviewFinished, setInterviewFinished] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [transcript, setTranscript] = useState("");

  const useTemplate = () => {
    setCompany(sampleData.company);
    setJobTitle(sampleData.jobTitle);
    setJobDescription(sampleData.jobDescription);
    console.log({ company, jobTitle, jobDescription });
  };

  useEffect(() => {
    console.log({ questions });
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
      console.log({ callId });
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
      console.log({ transcript });

      // Generate report card
      console.log({
        jobDescription,
        jobTitle,
        company,
        questions,
        overallRubric,
        transcript,
      });
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
      console.log({ reportCardData });
      setReportCard(reportCardData);
      console.log({ reportCard });

    } catch (error) {
      console.error("Error generating report card:", error);
    }
  };

  return (
    <Layout>
      <div className="hero min-h-screen bg-base-200">
        <div className="hero-content text-center">
          <div className="w-full max-w-4xl">
            <h1 className="text-5xl font-bold">Welcome to Dream Job! 🌟</h1>
            <p className="py-6">
              Prepare for your dream job with our mock interview platform.
              Practice, improve, and ace your interviews.
            </p>
            <div>
              <button className="btn btn-info mb-4" onClick={useTemplate}>
                Groq - Software Engineer, Developer Experience
              </button>
            </div>
            <div>
            <input
              type="text"
              placeholder="Company"
              value={company}
              onChange={(e) => setCompany(e.target.value)}
              className="input input-bordered w-full max-w-xs mb-4"
            />
            </div>
            <div>
            <input
              type="text"
              placeholder="Job Title"
              value={jobTitle}
              onChange={(e) => setJobTitle(e.target.value)}
              className="input input-bordered w-full max-w-xs mb-4"
            />
            </div>
            <div>
            <textarea
              placeholder="Job Description"
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
              className="textarea textarea-bordered w-full max-w-xs mb-4"
                rows="10"
              />
            </div>
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

            {questions && !reportCard && !isSubmitting && (
              <MdDisplay
                content={JSON.stringify(questions, null, 2)}
                title="Generated Questions"
              />
            )}
            {/* 
            {overallRubric && !isSubmitting && (
              <MdDisplay
                content={JSON.stringify(overallRubric, null, 2)}
                title="Overall Rubric"
              />
            )} */}
            {reportCard && !isSubmitting && (
              <ReportCardDisplay reportCardJSON={reportCard} />
            )}
          </div>
        </div>
      </div>
    </Layout>
  );
}
