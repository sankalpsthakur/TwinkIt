import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from get_emotion import get_emotion


# Read the CSV file
data = pd.read_csv('twitter_avaada.csv')

# Convert numeric columns to the correct data type
data['engagements'] = pd.to_numeric(data['engagements'], errors='coerce')
data['impressions'] = pd.to_numeric(data['impressions'], errors='coerce')
data['engagement rate'] = pd.to_numeric(data['engagement rate'], errors='coerce')
data['retweets'] = pd.to_numeric(data['retweets'], errors='coerce')
data['replies'] = pd.to_numeric(data['replies'], errors='coerce')
data['likes'] = pd.to_numeric(data['likes'], errors='coerce')

# Extract emotions from tweet text
# emotions_df = data['Tweet text'].apply(get_emotion).apply(pd.Series)
# Add the emotions columns to the main dataframe
data = pd.concat([data, emotions_df], axis=1)

# Combine date and time columns into a single datetime column
data['datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'])

# Extract hour and day of week
data['hour'] = data['datetime'].dt.hour
data['day_of_week'] = data['datetime'].dt.day_name()

data.to_csv('twitter_avaada_with_emotions.csv', index=False)

# Melt the emotions columns into a single column
emotion_data = data

print(emotion_data.head())

# Group by emotion and calculate mean engagement metrics
emotion_summary = emotion_data.groupby(['primary_emotion']).agg({
    'engagements': 'mean',
    'impressions': 'mean',
    'engagement rate': 'mean',
    'retweets': 'mean',
    'replies': 'mean',
    'likes': 'mean'
}).reset_index()

# Visualize the results
fig, ax = plt.subplots(figsize=(10, 6))
emotion_summary.pivot_table(index=['primary_emotion'], values=['engagements', 'impressions', 'engagement rate', 'retweets', 'replies', 'likes']).plot(kind='bar', ax=ax)
plt.title('Emotion Levels vs Engagement Metrics')
plt.xlabel('Emotion')
plt.ylabel('Mean Engagement Metrics')
plt.xticks(rotation=45)
plt.legend(title='Metrics')
plt.show()

# Group by hour and calculate mean engagement metrics
hour_summary = emotion_data.groupby(['hour']).agg({
    'engagements': 'mean',
    'impressions': 'mean',
    'engagement rate': 'mean',
    'retweets': 'mean',
    'replies': 'mean',
    'likes': 'mean'
}).reset_index()

#Visualize the results
fig, ax = plt.subplots(figsize=(10, 6))
hour_summary.pivot_table(index=['hour'], values=['engagements', 'impressions', 'engagement rate', 'retweets', 'replies', 'likes']).plot(kind='bar', ax=ax)
plt.title('Hour of Day vs Engagement Metrics')
plt.xlabel('Hour of Day')
plt.ylabel('Mean Engagement Metrics')
plt.xticks(rotation=45)
plt.legend(title='Metrics')
plt.show()

# THIS IS THE PLOT FOR THE EMOTION CHART
import matplotlib.pyplot as plt
import numpy as np

# Sample emotion data with engagement rates
emotion_data = {
    'Joy': {'angle': 0, 'engagement_rate': emotion_summary['engagement rate'][0]},
    'Trust': {'angle': 45, 'engagement_rate': emotion_summary['engagement rate'][1]},
    'Fear': {'angle': 90, 'engagement_rate': 250},
    'Surprise': {'angle': 135, 'engagement_rate': 100},
    'Sadness': {'angle': 180, 'engagement_rate': 175},
    'Disgust': {'angle': 225, 'engagement_rate': 60},
    'Anger': {'angle': 270, 'engagement_rate': 200},
    'Anticipation': {'angle': 315, 'engagement_rate': 110}
}

# Normalize engagement rates and map them to a range of radii
min_engagement = min(data['engagement_rate'] for data in emotion_data.values())
max_engagement = max(data['engagement_rate'] for data in emotion_data.values())
min_radius = 1
max_radius = 3

for emotion in emotion_data:
    normalized_engagement = (emotion_data[emotion]['engagement_rate'] - min_engagement) / (max_engagement - min_engagement)
    emotion_data[emotion]['radius'] = min_radius + normalized_engagement * (max_radius - min_radius)

# Function to convert polar to cartesian coordinates
def polar_to_cartesian(r, theta):
    x = r * np.cos(np.radians(theta))
    y = r * np.sin(np.radians(theta))
    return x, y

# Set up the plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)

# Plot emotions on the wheel
for emotion, data in emotion_data.items():
    x, y = polar_to_cartesian(data['radius'], data['angle'])
    ax.plot(np.deg2rad(data['angle']), data['radius'], 'o', markersize=20, label=emotion)

# Customize the plot
ax.set_rticks([])  # Hide radial ticks
ax.set_xticks(np.radians([data['angle'] for data in emotion_data.values()]))
ax.set_xticklabels(list(emotion_data.keys()))
ax.set_yticklabels([])
ax.spines['polar'].set_visible(False)

# Add a legend
ax.legend(loc=(1.1, 0.7), title='Emotions')

# Show the plot
plt.show()

