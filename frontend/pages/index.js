import { useState } from 'react';
import Layout from '../components/Layout';
import MdDisplay from '../components/MdDisplay'; // Import the new component

export default function Home() {
  const [dreamJob, setDreamJob] = useState('');
  const [cvContent, setCvContent] = useState('');
  const [questions, setQuestions] = useState('');
  const [isReadyForInterview, setIsReadyForInterview] = useState(false);
  const [conversationState, setConversationState] = useState('inactive'); // New state for conversation

  const generateCV = async () => {
    const response = await fetch(`http://127.0.0.1:8000/api/v1/doc_gen/generate_cv?job_title=${encodeURIComponent(dreamJob)}`, {
      method: 'POST',
      headers: {
        'accept': 'application/json',
      },
      body: '',
    });
    const data = await response.json();
    setCvContent(data.cv);
    return data.cv;
  };

  const generateQuestionsAndRubric = async (cv) => {
    const response = await fetch('http://127.0.0.1:8000/api/v1/doc_gen/generate_questions_and_rubric', {
      method: 'POST',
      headers: {
        'accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ cv }),
    });
    const data = await response.json();
    setQuestions(data.questions);
    setIsReadyForInterview(true);
  };

  const handleSubmit = async () => {
    try {
      const cv = cvContent || await generateCV();
      await generateQuestionsAndRubric(cv);
    } catch (error) {
      console.error('Error in the process:', error);
    }
  };

  const handleConversation = async () => {
    if (conversationState === 'inactive') {
      setConversationState('active');
      // Initiate conversation via API
      try {
        const response = await fetch('http://127.0.0.1:8000/api/v1/vapi/start', {
          method: 'POST',
          headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ questions }),
        });
        const data = await response.json();
        console.log('Conversation started:', data);
      } catch (error) {
        console.error('Error starting conversation:', error);
      }
    } else {
      setConversationState('inactive');
      // Stop conversation via API
      try {
        const response = await fetch('http://127.0.0.1:8000/api/v1/vapi/stop', {
          method: 'POST',
          headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({}),
        });
        const data = await response.json();
        console.log('Conversation stopped:', data);
      } catch (error) {
        console.error('Error stopping conversation:', error);
      }
    }
  };

  return (
    <Layout>
      <div className="hero min-h-screen bg-base-200">
        <div className="hero-content text-center">
          <div className="max-w-md">
            <h1 className="text-5xl font-bold">Welcome to Dream Job! 🌟</h1>
            <p className="py-6">Prepare for your dream job with our mock interview platform. Practice, improve, and ace your interviews.</p>
            <input
              type="text"
              placeholder="Startup Enhancement Specialist"
              value={dreamJob}
              onChange={(e) => setDreamJob(e.target.value)}
              className="input input-bordered w-full max-w-xs mb-4"
            />
            <textarea
              placeholder="Paste your CV content here... (optional)"
              value={cvContent}
              onChange={(e) => setCvContent(e.target.value)}
              className="textarea textarea-bordered w-full max-w-xs mb-4"
              rows="10"
            />
            <div className="flex justify-center">
              <button className="btn btn-primary" onClick={handleSubmit}>Submit</button><br />
              {isReadyForInterview && (
                <button className="btn btn-secondary mt-4" onClick={handleConversation}>
                  {conversationState === 'inactive' ? 'Start Interview' : 'Stop Interview'}
                </button>
              )}
            </div>

            {cvContent && <MdDisplay content={cvContent} title="Generated CV" />}
            {questions && <MdDisplay content={questions} title="Generated Questions" />}
          </div>
        </div>
      </div>

      <div id="projects" className="p-4">
        <h2 className="text-4xl font-bold text-center mb-6">Features</h2>
        <p className="text-center mb-6">
          Our platform offers a variety of mock interview scenarios tailored to your dream job. Get feedback and improve your skills.
        </p>
        <p className="text-center mb-6">
          Key features include: realistic interview questions, instant feedback, progress tracking, and more.
        </p>
      </div>
    </Layout>
  )
}