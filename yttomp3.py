import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

def download_youtube_video(youtube_url, output_path):
    try:
        yt = YouTube(youtube_url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=output_path)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(f"Downloaded and converted to MP3: {new_file}")
        return new_file
    except Exception as e:
        print(f"Error: {e}")
        return None

def convert_to_mp3(video_path):
    try:
        video_clip = VideoFileClip(video_path)
        audio_path = os.path.splitext(video_path)[0] + '.mp3'
        video_clip.audio.write_audiofile(audio_path)
        video_clip.close()
        print(f"Converted to MP3: {audio_path}")
        return audio_path
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube URL: ")
    output_path = input("Enter the output path (leave blank for current directory): ") or "."
    
    mp3_file = download_youtube_video(youtube_url, output_path)
    if mp3_file:
        print(f"MP3 file saved at: {mp3_file}")
    else:
        print("Failed to download or convert the video.")
