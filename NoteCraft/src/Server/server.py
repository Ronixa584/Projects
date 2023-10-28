# from flask import Flask, request, jsonify
# import requests
# from pytube import YouTube
# from pydub import AudioSegment
# import speech_recognition as sr
# import io

# app = Flask(_name_)

# @app.route('/transcribe', methods=['POST'])
# def transcribe():
#     video_url = request.json.get('videoUrl')

#     yt = YouTube(video_url)
#     stream = yt.streams.filter(only_audio=True).first()
#     audio_stream_url = stream.url

#     response = requests.get(audio_stream_url)
#     audio = AudioSegment.from_file(io.BytesIO(response.content), format="mp4")

#     recognizer = sr.Recognizer()

#     with sr.AudioFile(io.BytesIO(audio.raw_data), sample_rate=audio.frame_rate) as source:
#         audio = recognizer.record(source)

#     try:
#         transcription = recognizer.recognize_google(audio)
#         return jsonify({"transcription": transcription})
#     except sr.UnknownValueError:
#         return jsonify({"error": "Google Web Speech API could not understand the audio"})
#     except sr.RequestError as e:
#         return jsonify({"error": f"Could not request results from Google Web Speech API; {e}"}), 500

# if _name_ == '_main_':
#     app.run(debug=True)

# Update the Flask server code
# from flask import Flask
# https://www.youtube.com/watch?v=uR14UROzm-c
# https://www.youtube.com/watch?v=t-ZggDz_GUo
# Internet Speed is necessary


from flask import Flask, request, jsonify
import requests
from pytube import YouTube
from pydub import AudioSegment
# from pydub import AudioSegment
AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffplay.exe"
AudioSegment.ffprobe ="C:\\ffmpeg\\bin\\ffprobe.exe"
import speech_recognition as sr
import io
from flask_cors import CORS
import time



app = Flask(__name__)
CORS(app)

CORS(app, resources={r"/VideoTranscription": {"origins": "http://localhost:1234"}})

@app.route('/')
def index():
    return "Hello, World!"



@app.route('/VideoTranscription', methods=['POST'])
def transcribe():
    print("Welcome")
    try:
        # print("Wk")
        data = request.json
        video_url = data.get('videoUrl')

        if not video_url:
            return jsonify({"error": "Missing videoUrl parameter"}), 400

        print("Received POST request to /VideoTranscription 1")

        yt = YouTube(video_url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download(output_path='Downloads', filename="video.mp4")
        audio_stream_url = stream.url
        
        print("Received POST request to /VideoTranscription 2")

        response = requests.get(audio_stream_url)
        
        print("Received POST request to /VideoTranscription 2")
        
        # audio = AudioSegment.from_file(io.BytesIO(response.content), format="mp4")
        audio = AudioSegment.from_file("Downloads/video.mp4")
        
        audio.export("Downloads/audio.wav", format="wav")

        recognizer = sr.Recognizer()
        
        print("Received POST request to /VideoTranscription 3")
         
        # time.sleep(15)
        with sr.AudioFile("downloads/audio.wav") as source:
            audio = recognizer.record(source)
            
        print("Received POST request to /VideoTranscription 4")

        try:
            transcription = recognizer.recognize_google(audio)
            return jsonify({"transcription": transcription})
        except sr.UnknownValueError:
            return jsonify({"error": "Google Web Speech API could not understand the audio"})
        except sr.RequestError as e:
            return jsonify({"error": f"Could not request results from Google Web Speech API; {e}"}), 500
    except Exception as e:
        print("Received POST request to /VideoTranscription Error in SERVER")
        return jsonify({"error": f"An error occurred: {e}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
