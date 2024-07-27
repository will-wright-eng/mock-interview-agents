import React from 'react';
import ReactMarkdown from 'react-markdown';

const MdDisplay = ({ content, title }) => {
  return (
    <div className="mt-6 p-6 bg-white shadow-lg rounded-lg">
      <h2 className="text-3xl font-bold mb-4">{title}</h2>
      <div className="prose">
        <ReactMarkdown>{content}</ReactMarkdown>
      </div>
    </div>
  );
};

export default MdDisplay;