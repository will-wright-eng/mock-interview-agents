import { useState } from 'react';
import Layout from '../components/Layout';

export default function Home() {
  const [dreamJob, setDreamJob] = useState('');

  const handleSubmit = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/dream-job', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ job: dreamJob }),
      });
      const data = await response.json();
      console.log('Response:', data);
    } catch (error) {
      console.error('Error submitting dream job:', error);
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
            <button className="btn btn-primary" onClick={handleSubmit}>Submit</button>
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