import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import datetime
import os
import logging as console

console.basicConfig(filename="youtube_logs.log", level=console.INFO, \
                    format="%(asctime)s %(name)s %(levelname)s %(message)s")

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

# Function to convert seconds to HH:MM:SS format
def format_timestamp(seconds):
    return str(datetime.timedelta(seconds=int(seconds)))

# Function to get and format the transcript
def get_formatted_transcript(video_id):
    console.info('Getting video transcript')
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    formatted_transcript = ""

    for entry in transcript:
        start = format_timestamp(entry['start'])
        text = entry['text']
        formatted_transcript += f"Timestamp: {start}\nTranscription: {text}\n\n"
    return formatted_transcript

def get_gemini_timestamps(transcript, prompt):
    console.info('Getting Gemini Response for Topics')
    response = model.generate_content(prompt + transcript)
    return response.text

def get_gemini_summary(transcript, prompt):
    console.info('Getting Gemini Response for Summary')
    response = model.generate_content(prompt + transcript)
    return response.text




