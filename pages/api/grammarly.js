import { checkGrammar } from '../../services/grammarly';

export default async function handler(req, res) {
  if (req.method === 'POST') {
    try {
      const text = req.body.text;
      const result = await checkGrammar(text);
      res.status(200).json(result);
    } catch (error) {
      res.status(500).json({ error: 'An error occurred while processing the request.' });
    }
  } else {
    res.status(405).json({ error: 'Method not allowed.' });
  }
}
