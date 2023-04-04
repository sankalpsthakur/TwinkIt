import React from 'react';

const ToolSelector = ({ selectedTool, onChange }) => {
  return (
    <select value={selectedTool} onChange={onChange}>
      <option value="grammarly">Grammarly</option>
      <option value="tweet-writer">Tweet Writer</option>
    </select>
  );
};

export default ToolSelector;
