# AI Video Summarizer 🎬🧠

Welcome to AI Video Summarizer — a functional, lightweight project designed to generate concise summaries from YouTube videos using OpenAI’s powerful language models. The goal is to simplify long videos into easily digestible information. While it’s an early version, the app is fully functional with a valid API key.

---

## Features ✨🚀
- Input a YouTube URL and receive a clean, AI-generated summary.
- Uses `youtube_transcript_api` to extract transcripts.
- OpenAI GPT API for natural language summarization.
- Flask-powered backend with a simple and clean front-end.
- Easy to run and extend!

---

## Tech Stack ⚙️💻
- Python 3.x
- Flask
- HTML & CSS
- OpenAI GPT API
- youtube_transcript_api

---

## Visuals 🖼️📸

Below are screenshots demonstrating the app in action:

![Demo Image](https://github.com/udaycodespace/yt_summarizer/blob/master/screenshot1.png)


![Screenshot 1](https://github.com/udaycodespace/yt_summarizer/blob/master/demo_image.png)

---

## How to Run 🏃‍♂️🧪

1. Clone the repository:
   ```bash
   git clone https://github.com/udaycodespace/yt_summarizer.git
   cd yt_summarizer
   ```

2. Add your OpenAI API key in the designated line in `app.py`.

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch the application:
   ```bash
   python app.py
   ```

5. Open your browser and visit:
   ```
   http://localhost:5000
   ```

---

## Project Status 📌🔧

This project is in an early but working state. Although not production-ready, it serves as a functional prototype. You’ll need to provide your own OpenAI API key to access the summarization features. Screenshots above prove that it worked successfully during prior testing with a valid key.

---

## Contributing 🤝💡

Feel free to fork, improve, or suggest features through issues or PRs. Collaboration is welcome!

---

## License 📃📝

This project is licensed under the MIT License — use it freely and contribute back if you find it useful.

---

## Final Note 🧠💬

AI Video Summarizer is built to bridge the gap between long-form video content and summarized knowledge, enabling faster and smarter content consumption.
