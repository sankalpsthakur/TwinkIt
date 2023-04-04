import axios from 'axios';

export async function checkGrammar(text) {
  try {
    // Replace with the actual API call to Grammarly
    const response = await axios.post('https://your-grammarly-api-endpoint', {
      text,
    });

    return response.data;
  } catch (error) {
    console.error('Error in Grammarly API:', error);
    throw error;
  }
}
