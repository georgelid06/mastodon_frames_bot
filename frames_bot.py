import time
import subprocess
import os
from mastodon import Mastodon

# Authenticate with Mastodon
mastodon = Mastodon(
    client_id='your_client_id', client_secret='your_client_secret', access_token='your_access_token', api_base_url=instance_url
)

# Set video and subtitle files
video_file = 'path/to/your/video/file'
subtitle_file = 'path/to/your/subtitle/file'

#Set these as desired
frames_per_second = 1 #how many frames of each second are extracted, for the Hobbit bot its set at 2
frame_interval = 15 #set this to the minutes you want between each post
film_name = "Insert film name here"

ffprobe_output = subprocess.check_output([
    'ffprobe',
    '-v', 'error',
    '-show_entries', 'format=duration',
    '-of', 'default=noprint_wrappers=1:nokey=1',
    video_file
]).decode('utf-8').strip()
movie_duration = int(float(ffprobe_output))

total_frames = movie_duration * frames_per_second

def post_frame(frame_number):
    frame_file = f'frame-{frame_number:04d}.png'

    # Generate frame image
    subprocess.run([
        'ffmpeg',
        '-ss', str(frame_number),
        '-i', video_file,
        '-vf', f"fps={frames_per_second},subtitles={subtitle_file}:force_style='Fontsize=24,PrimaryColour=&HFFFFFF'",
        '-frames:v', '1',
        frame_file
    ])


    # Post the frame with the caption
    with open(frame_file, 'rb') as media:
        caption = f'{film_name} - Frame {frame_number} of {total_frames}'
        mastodon.status_post(caption, media_ids=[mastodon.media_post(media).id])

    # Clean up the generated frame file
    os.remove(frame_file)

frame_number = 1
frame_interval = frame_interval * 60 # to convert to seconds 

while frame_number <= total_frames:
    post_frame(frame_number)
    frame_number += 1
    time.sleep(frame_interval)
