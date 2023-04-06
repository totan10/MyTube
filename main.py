from pytube import YouTube, Playlist
from moviepy.editor import *
import os


def download_video():
    url = input("Enter the YouTube video URL: ")
    path = input("Enter the file path to save the video: ")
    try:
      video = YouTube(url)
      print("Title:", video.title)
      print("Length:", video.length, "seconds")
      print("Available formats:")
      for stream in video.streams.filter(progressive=True):
          print(stream.resolution, stream.mime_type)
      resolution = input("Enter the preferred resolution (e.g. 720p): ")
      format = input("Enter the preferred format (e.g. mp4): ")
      stream = video.streams.filter(
          resolution=resolution, mime_type=f"video/{format}").first()
      filename = video.title.replace(" ", "_") + "." + format
      stream.download(output_path=path, filename=filename)
      print("Video downloaded successfully!")
    except Exception as e:
        print("An error occurred:", e)


def download_audio():
  url = input("Enter the YouTube video URL: ")
  path = input("Enter the file path to save the audio: ")
  try:
    video = YouTube(url)
    print("Title:", video.title)
    print("Length:", video.length, "seconds")
    print("Available formats:")
    for stream in video.streams.filter(only_audio=True):
        print(stream.abr, stream.mime_type)
    format = input("Enter the preferred format (e.g. mp3): ")
    stream = video.streams.filter(
        only_audio=True, mime_type=f"audio/{format}").first()
    filename = video.title.replace(" ", "_") + "." + format
    stream.download(output_path=path, filename=filename)
    print("Audio downloaded successfully!")
  except Exception as e:
      print("An error occurred:", e)


def download_video_playlist():
    url = input("Enter the YouTube playlist URL: ")
    path = input("Enter the file path to save the playlist: ")
    playlist = Playlist(url)
    print("Playlist Title:", playlist.title())
    print("Number of videos in playlist:", len(playlist.video_urls))
    resolution = input("Enter the preferred resolution (e.g. 720p): ")
    format = input("Enter the preferred format (e.g. mp4): ")
    for video_url in playlist.video_urls:
        try:
            video = YouTube(video_url)
            stream = video.streams.filter(
                resolution=resolution, mime_type=f"video/{format}").first()
            filename = video.title.replace(" ", "_") + "." + format
            stream.download(output_path=path, filename=filename)
            print(f"Video '{video.title}' downloaded successfully!")
        except Exception as e:
            print(f"An error occurred while downloading '{video.title}': {e}")
            continue
    print("Playlist downloaded successfully!")


def download_audio_playlist():
    url = input("Enter the YouTube playlist URL: ")
    path = input("Enter the file path to save the playlist: ")
    playlist = Playlist(url)
    print("Playlist Title:", playlist.title())
    print("Number of videos in playlist:", len(playlist.video_urls))
    format = input("Enter the preferred format (e.g. mp3): ")
    for video_url in playlist.video_urls:
        try:
            video = YouTube(video_url)
            stream = video.streams.filter(
                only_audio=True, mime_type=f"audio/{format}").first()
            filename = video.title.replace(" ", "_") + "." + format
            stream.download(output_path=path, filename=filename)
            print(f"Audio '{video.title}' downloaded successfully!")
        except Exception as e:
            print(f"An error occurred while downloading '{video.title}': {e}")
            continue
    print("Playlist downloaded successfully!")


def video_to_audio():
  video_file = input("Enter the video file with complete path: ")
  audio_file = input("Enter the output audio file name: ")
  try:
    video = VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(audio_file)
    audio.close()
    video.close()
    print("Video converted to audio successfully!")
  except Exception as e:
    print(f"An error occurred while converting : {e}")


def video_to_gif():
  video_file = input("Enter the video file name with complete path: ")
  try:
    gif_file = os.path.splitext(video_file)[0] + ".gif"
    start_time = input("Enter the start time in seconds (e.g. 10.5): ")
    end_time = input("Enter the end time in seconds (e.g. 20.5): ")
    video = VideoFileClip(video_file)
    gif = video.subclip(float(start_time), float(end_time)).resize(height=320)
    gif.write_gif(gif_file)
    gif.close()
    video.close()
    print("Video converted to GIF successfully!")
  except Exception as e:
      print("An error occurred:", e)


def merge_videos():
  try:
        n = int(input("Enter the number of videos to merge: "))
        clips = []
        for i in range(n):
            video_path = input(f"Enter the path of video #{i+1}: ")
            clip = VideoFileClip(video_path)
            clips.append(clip)
        file_path = input("Enter the path to save the merged video file (without extension): ")
        file_name = input("Enter the name of the merged video file (with extension): ")
        output_path = os.path.join(file_path, file_name)
        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile(output_path)
        print("Videos merged successfully!")
  except Exception as e:
      print("An error occurred:", e)


while True:
  try:
    print("""
    Welcome to MyTube!!!!!!!                                                                                                        

    Please choose an option:
    1. Download video
    2. Download audio
    3. Download video playlist
    4. Download audio playlist
    5. Convert video to audio
    6. Convert video to GIF
    7. Merge videos
    0. Exit
    """)
    choice = input("Enter your choice: ")

    if choice == "1":
        download_video()
    elif choice == "2":
        download_audio()
    elif choice == "3":
        download_video_playlist()
    elif choice == "4":
        download_audio_playlist()
    elif choice == "5":
        video_to_audio()
    elif choice == "6":
        video_to_gif()
    elif choice == "7":
        merge_videos()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please enter a number from 0 to 7.")

  except Exception as e:
    print("An error occurred:", e)
    continue
