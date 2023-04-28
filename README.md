# Every Frame of xxx Bot

This Python script allows you to post frames from a film (or TV show) to a mastodon account. The script is customizable, allowing you to set the number of frames per second and the time interval between posts.

## Prerequisites

- Python 3
- FFmpeg
- A Mastodon account

## Setup

1. Install the required Python packages:

```
pip install Mastodon.py
```
2. Create a Mastodon account on your desired instance (e.g., mastodon.social) and log in.

3. Visit the "Development" section under your account settings and create a new application. Take note of the generated `client_id`, `client_secret`, and `access_token`.

4. Replace the placeholders in the script with the appropriate values:

- `your_client_id`: Your Mastodon application's client ID
- `your_client_secret`: Your Mastodon application's client secret
- `your_access_token`: Your Mastodon account's access token
- `instance_url`: The URL of your Mastodon instance (e.g., 'https://mastodon.social')
- `path/to/your/video/file`: The path to your video file
- `path/to/your/subtitle/file`: The path to your subtitle file

5. Customize the following variables as desired:

- `frames_per_second`: The number of frames to extract from each second of the video
- `frame_interval`: The time interval (in minutes) between each post
- `film_name`: The name of the film being processed

## Running the Script

Run the script using Python:
```
python frames_bot.py
```
The script will start posting frames to your Mastodon account according to the specified settings. To stop the script, press `Ctrl + C` in the terminal.
I have this on a server running continuously but I know another way is to make the code post one frame and task schedule it to run every x minutes
