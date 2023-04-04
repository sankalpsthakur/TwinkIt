import React from 'react';

const TweetWriter = ({ tweets }) => {
  if (!tweets || tweets.length === 0) {
    return <p>No tweets generated yet.</p>;
  }

  return (
    <div className="tweet-writer">
      {tweets.map((tweet, index) => (
        <div key={index} className="tweet">
          {tweet}
        </div>
      ))}
    </div>
  );
};

export default TweetWriter;
