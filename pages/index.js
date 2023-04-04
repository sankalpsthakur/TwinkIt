import { useState } from 'react';
import Editor from '../components/Editor';
import Output from '../components/Output';
import ToolSelector from '../components/ToolSelector';
import TweetWriter from '../components/TweetWriter';

export default function Home() {
  const [text, setText] = useState('');
  const [tool, setTool] = useState('grammarly');
  const [result, setResult] = useState('');
  const [tweets, setTweets] = useState([]);

  const handleTextChange = (event) => {
    setText(event.target.value);
  };

  const handleToolChange = (event) => {
    setTool(event.target.value);
  };

  const handleSubmit = async () => {
    if (tool === 'grammarly') {
      // Call Grammarly API
    } else if (tool === 'tweet-writer') {
      // Call Tweet Writer API
    }
  };

  return (
    <div className="container">
      <h1>Writing CMS</h1>
      <ToolSelector selectedTool={tool} onChange={handleToolChange} />
      <Editor value={text} onChange={handleTextChange} />
      <button onClick={handleSubmit}>Submit</button>
      <Output result={result} />
      <TweetWriter tweets={tweets} />
    </div>
  );
}
