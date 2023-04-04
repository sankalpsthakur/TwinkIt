import React from 'react';

const Output = ({ result }) => {
  return (
    <div className="output">
      <p>{result || 'Output will be displayed here...'}</p>
    </div>
  );
};

export default Output;
