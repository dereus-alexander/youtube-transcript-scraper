YouTube Playlist Transcript Extractor

This Python script extracts transcripts from all videos in a YouTube playlist and saves them to a single text file. It then allows you to easily summarize the content of the playlist using Large Language Models (LLMs) like ChatGPT, Google Bard, or Claude.

## Features

- Automatically fetches all video URLs from a given YouTube playlist.
- Retrieves transcripts for each video.
- Handles cases where transcripts are disabled or unavailable.
- Saves all transcripts to a single, well-formatted text file.
- Includes error handling and rate limiting to avoid issues with the YouTube API.

## Prerequisites

- **Python 3.6 or higher:** Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
- **`pytube` library:** Used for accessing YouTube playlist information.
- **`youtube-transcript-api` library:** Used for retrieving video transcripts.

## Installation

1. **Clone this repository (or download the `youtube_playlist_transcript.py` file):**
  
  ```bash
  git clone https://github.com/YourUsername/youtube-playlist-transcript-tool.git  # Replace with your repo URL
  cd youtube-playlist-transcript-tool
  ```
  
2. **Install the required Python libraries using pip:**
  
  ```bash
  pip install pytube youtube-transcript-api
  ```
  
  If you encounter permissions issues, you might need to use `pip install --user pytube youtube-transcript-api` or run the command with administrator privileges.
  

## Usage

1. **Run the script:**
  
  ```bash
  python youtube_playlist_transcript.py
  ```
  
2. **Enter the YouTube playlist URL when prompted:**
  
  The script will ask you to enter the URL of the YouTube playlist you want to extract transcripts from. Make sure to copy and paste the full URL (e.g., `https://www.youtube.com/playlist?list=PLG49S3nxzAnl_tQe3kvnmeMid0mjF8Le8`).
  
3. **Wait for the script to complete:**
  
  The script will iterate through each video in the playlist, retrieve the transcript (if available), and save it to a file named `playlist_transcripts.txt` in the same directory as the script. The script will print progress messages to the console as it processes each video. It also handles errors and rate limits, so it might take some time to complete for large playlists. Error messages are printed to `stderr`.
  
4. **Summarize with an LLM (Large Language Model):**
  
  - Open the `playlist_transcripts.txt` file.
  - Copy the entire contents of the file.
  - Paste the contents into an LLM like ChatGPT, Google Bard, or Claude.
  - Use a prompt to guide the LLM to summarize the content. Examples:
    - "Summarize the key concepts presented in this document."
    - "Provide a list of t- - he main takeaways from this series of videos."
  - "Extract the most important arguments presented in this debate and provide a summary of each argument."
- The LLM will generate a summary of the playlist content.  
