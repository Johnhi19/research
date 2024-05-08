from flask import Flask, render_template, jsonify
from spotify_script import get_token, request_valid_song
import os

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/get-song', methods=['POST'])
def get_song():
    access_token = get_token()
    song_details = request_valid_song(access_token)
    return jsonify(song_details)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    application.run(host="0.0.0.0",debug=True,port=port)
