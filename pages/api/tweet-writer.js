import { generateTweets } from '../../services/tweetWriter';

export default async function handler(req, res) {
  if (req.method === 'POST') {
    try {
      const text = req.body.text;
      const tweets = await generateTweets(text);
      res.status(200).json(tweets);
    } catch (error) {
      res.status(500).json({ error: 'An error occurred while processing the request.' });
    }
  } else {
    res.status(405).json({ error: 'Method not allowed.' });
  }
}
