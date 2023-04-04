import Airtable from 'airtable';

const base = new Airtable({ apiKey: process.env.AIRTABLE_API_KEY }).base(
  process.env.AIRTABLE_BASE_ID
);

export async function saveToAirtable(text, result) {
  try {
    await base('Table_Name').create([
      {
        fields: {
          'Input Text': text,
          'Processed Text': result,
        },
      },
    ]);
  } catch (error) {
    console.error('Error saving to Airtable:', error);
  }
}
