from pytube import Playlist, exceptions as pytube_exceptions
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import time
import os  # Import the os module
from youtube_transcript_api import (
    TranscriptsDisabled,
    NoTranscriptFound,
    CouldNotRetrieveTranscript,
    TooManyRequests
)
import sys #Import sys module

def get_playlist_videos(playlist_url):
    """
    Retrieves a list of video URLs from a YouTube playlist.

    Args:
        playlist_url (str): The URL of the YouTube playlist.

    Returns:
        list: A list of video URLs, or None if an error occurred.
    """
    try:
        playlist = Playlist(playlist_url)
        # Attempt to access the playlist to trigger exceptions early
        playlist.video_urls
        return list(playlist.video_urls)  # Convert to list to avoid generator issues later
    except pytube_exceptions.RegexMatchError as e:
        print(f"Error: Invalid playlist URL. Please check the URL.\nDetails: {e}", file=sys.stderr)  #Print to stderr
        return None
    except pytube_exceptions.PytubeError as e:  # Catch other pytube exceptions
         print(f"Error accessing playlist: {e}", file=sys.stderr) #Print to stderr
         return None
    except Exception as e:
        print(f"An unexpected error occurred while fetching the playlist: {e}", file=sys.stderr) #Print to stderr
        return None


def get_video_transcript(video_id):
    """
    Retrieves the transcript for a given YouTube video.

    Args:
        video_id (str): The ID of the YouTube video.

    Returns:
        str: The transcript text, or None if no transcript is available or an error occurred.
    """
    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Format the transcript into plain text
        formatter = TextFormatter()
        transcript_text = formatter.format_transcript(transcript)

        return transcript_text
    except TranscriptsDisabled as e:
        print(f"Transcript is disabled for video {video_id}.", file=sys.stderr) #Print to stderr
        return None
    except NoTranscriptFound as e:
        print(f"No transcript found for video {video_id}.", file=sys.stderr) #Print to stderr
        return None
    except CouldNotRetrieveTranscript as e:
        print(f"Could not retrieve transcript for video {video_id}: {e}", file=sys.stderr) #Print to stderr
        return None
    except TooManyRequests as e:
        print(f"Too many requests to YouTube API.  Consider adding a longer delay. Video ID: {video_id}", file=sys.stderr) #Print to stderr
        return None
    except Exception as e:
        print(f"Could not retrieve transcript for video {video_id}: {e}", file=sys.stderr) #Print to stderr
        return None


def save_transcripts_to_file(playlist_url, output_file):
    """
    Retrieves and saves transcripts from a YouTube playlist to a text file.

    Args:
        playlist_url (str): The URL of the YouTube playlist.
        output_file (str): The name of the output file to save the transcripts to.
    """

    video_urls = get_playlist_videos(playlist_url)

    if video_urls is None:
        print("Aborting transcript saving due to playlist error.", file=sys.stderr) #Print to stderr
        return

    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for i, video_url in enumerate(video_urls):
                video_id = video_url.split('v=')[1]
                transcript = get_video_transcript(video_id)

                if transcript:
                    progress_message = f"Transcript for video {i+1}/{len(video_urls)}: {video_url}"
                    print(progress_message)
                    sys.stdout.flush() # Force the output to print to the console immediately
                    file.write(f"{progress_message}\n")
                    file.write(transcript)
                    file.write("\n\n")
                else:
                    no_transcript_message = f"No transcript available for video {i+1}/{len(video_urls)}: {video_url}"
                    print(no_transcript_message, file=sys.stderr) #Print to stderr
                    sys.stderr.flush() #Force the error output
                    file.write(f"{no_transcript_message}\n\n")

                time.sleep(1)  # Add a delay to avoid rate limiting
        print(f"Transcripts saved to {output_file}")
        sys.stdout.flush()

    except Exception as e:
        print(f"An error occurred while writing to the file: {e}", file=sys.stderr) #Print to stderr
        sys.stderr.flush()
        if os.path.exists(output_file):
            print(f"Partial transcripts may have been saved to {output_file}", file=sys.stderr) #Print to stderr
            sys.stderr.flush()
        else:
            print("No transcript file was created.", file=sys.stderr) #Print to stderr
            sys.stderr.flush()


if __name__ == "__main__":
    # Input: YouTube playlist URL
    playlist_url = input("Enter the YouTube playlist URL: ")

    # Output: Text file to save transcripts
    output_file = "playlist_transcripts.txt"

    # Save transcripts to file
    save_transcripts_to_file(playlist_url, output_file)
