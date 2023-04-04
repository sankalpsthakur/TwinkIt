from flask import Flask, request, jsonify
import tweet_writer

app = Flask(__name__)

@app.route('/api/tweet-writer', methods=['POST'])
def generate_tweets():
    text = request.json.get('text', '')
    tweets = tweet_writer.generate_tweets(text)
    return jsonify(tweets)

if __name__ == '__main__':
    app.run()
