import streamlit as st
import time
import os
from fx import mk_base, download_audio, LyscnDir
from io import BytesIO
from pathlib import Path

# METAINFO = {
#     "title": "Lyscn",
#     "icon": "🌊",
#     "dir": "/audio"
# }
# audio_dir = Path.home() / "Lyscn" / "Audio"
# audio_dir = Path.cwd() / "Audio"
# audio_dir.mkdir(parents=True, exist_ok=True)




# def handle_music_search(query: str):
    
#     formatted_result = ""
#     for index, song in enumerate(results):
#         formatted_result = formatted_result + f"""
# {index+1}. {song["title"]} _by_ {song["artists"][0]["name"]}
# _Link:_ https://music.youtube.com/watch?v={song["videoId"]}
# """
#     return formatted_result


def yt_download_song(link: str):
    # ytmusic.get_song(link)
    # mk_base()
    audio_info = download_audio(link)
    # st.json(audio_info)
    filename = f"{audio_info['title']}.{audio_info['ext']}"
    filepath = f"./audio.{audio_info['ext']}"
    print("filepath", filepath)
    st.code(f"{filename}")
    print("filepath exists", os.path.exists(filepath))
    if os.path.exists(filepath):
        with open(filepath, "rb") as fileopener:
            if st.download_button(
                label="Download",
                data=fileopener,
                file_name=filename,
                mime=f"audio/{audio_info['ext']}"
            ):
                st.toast(f"Downloading: {filename}")
        os.remove(filepath)

st.write("Download YouTube Audio")
link_input = st.text_input(label="Link")
download_button = st.button("Get")
if download_button:
    if bool(link_input):
        with st.spinner("Downloading...", show_time=True):
            yt_download_song(link_input)
    else:
        st.toast(":red[*] Please provide a YouTube Link")