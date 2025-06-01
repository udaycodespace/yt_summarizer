import os
from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
import openai

app = Flask(__name__)

openai.api_key = "OPENAI_API_KEY" ##Use Your API KEY with enough credits!

def get_video_id(url):
    from urllib.parse import urlparse, parse_qs
    query = urlparse(url)
    if query.hostname in ["youtu.be"]:
        return query.path[1:]
    if query.hostname in ["www.youtube.com", "youtube.com"]:
        if query.path == "/watch":
            return parse_qs(query.query).get("v", [None])[0]
        if query.path.startswith("/embed/"):
            return query.path.split("/")[2]
        if query.path.startswith("/v/"):
            return query.path.split("/")[2]
    return None

def fetch_transcript(video_id):
    """
    Attempts to fetch the transcript for the given video_id.
    If any error occurs (no transcript, video blocked, etc.), returns None.
    """
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry["text"] for entry in transcript_list])
    except Exception:
        return None

def summarize_text(text):
    """
    Calls OpenAI’s v1.0+ chat completion to summarize `text`.
    Returns a string summary or an error message.
    """
    if not openai.api_key:
        return "Error: OpenAI API key not found in code."

    if not text or text.strip() == "":
        return "Transcript not available."

    prompt = (
        "You are a helpful assistant. "
        "Please provide a concise summary (3–5 sentences) "
        "of the following YouTube video transcript:\n\n"
        f"{text}\n\n"
        "Summary:"
    )

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=300,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error calling OpenAI API: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    if request.method == "POST":
        url_in = request.form.get("url", "").strip()
        video_id = get_video_id(url_in)
        if video_id:
            transcript = fetch_transcript(video_id)
            summary = summarize_text(transcript)
        else:
            summary = "Invalid YouTube URL"
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
