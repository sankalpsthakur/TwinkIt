import React from 'react';

const Editor = ({ value, onChange }) => {
  return (
    <textarea
      className="editor"
      value={value}
      onChange={onChange}
      placeholder="Type your text here..."
    />
  );
};

export default Editor;
