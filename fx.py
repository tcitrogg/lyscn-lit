"""
Functions for Lyscn
"""

import yt_dlp
import os
from pathlib import Path

home_dir = Path.home()
# print(home_dir)
LyscnDir = {
    "base": f"{home_dir}/Lyscn",
    "video": f"{home_dir}/Lyscn/Video",
    "audio": f"{home_dir}/Lyscn/Audio",
}

# create the dir if not exist
def mk_base():
    os.makedirs(LyscnDir['audio'], exist_ok=True)
    os.makedirs(LyscnDir['video'], exist_ok=True)

def download_video(yt_link: list):
    """yt_link: list
    """
    ydl_opts = {
        "format": "best",
        "quiet": False,
        "outtmpl": f"{LyscnDir['video']}/%(title)s.%(ext)s",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as yt_downloader:
        yt_downloader.download([*yt_link])

def download_audio(yt_link: list):
    """yt_link: list
    """
    ydl_opts = {
        "format": "m4a/bestaudio",
        "quiet": False,
        "outtmpl": f"{LyscnDir['audio']}/%(title)s.%(ext)s",
        # "postprocessors": [{
        #     "key": "FFmpegExtractAudio",
        #     "preferredcodec": "m4a"
        # }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as yt_downloader:
        yt_downloader.download([*yt_link])

def shazam_audio(yt_link: str):
    ...