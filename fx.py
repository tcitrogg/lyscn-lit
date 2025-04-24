"""
Functions for Lyscn
"""

import os
import yt_dlp

from pathlib import Path
from ytmusicapi import YTMusic


home_dir = Path.home()
ytmusic = YTMusic()
# print(home_dir)
audio_dir = Path.cwd() / "Audio"
LyscnDir = {
    "base": f"{home_dir}/Lyscn",
    "video": f"{home_dir}/Lyscn/Video",
    "audio": "./Audio",
}


# create the dir if not exist
def mk_base():
    # os.makedirs(LyscnDir['audio'], exist_ok=True)
    # os.makedirs(LyscnDir['video'], exist_ok=True)
    audio_dir.mkdir(parents=True, exist_ok=True)

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

def download_audio(yt_link: str, format="m4a/bestaudio", quiet=True):
    """yt_link: list
    """
    ydl_opts = {
        "format": format,
        "quiet": quiet,
        "outtmpl": f"audio.%(ext)s",
        # "outtmpl": f"{LyscnDir['audio']}/%(title)s.%(ext)s",
        # "filename": "%(title)s.%(ext)s",
        "quiet": quiet
        # "postprocessors": [{
        #     "key": "FFmpegExtractAudio",
        #     "preferredcodec": "m4a"
        # }],
        # 'merge_output_format': 'mp4'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as yt_downloader:
        audio_info = yt_downloader.extract_info(url=yt_link, download=True)
        # yt_downloader.download([*yt_link])
    return audio_info

def shazam_audio(yt_link: str):
    ...

def search_ytaudio(query: str, filter="songs", limit=100):
    results = ytmusic.search(query=query, filter=filter, limit=limit)
    return results