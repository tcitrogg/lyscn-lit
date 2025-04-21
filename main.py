import streamlit as st
import time
from ytmusicapi import YTMusic
from fx import mk_base, download_audio

METAINFO = {
    "title": "Lyscn",
    "icon": "🌊",
    "dir": "/audio"
}

ytmusic = YTMusic()



def handle_music_search(query: str):
    results = ytmusic.search(query, filter="songs", limit=100)
    formatted_result = ""
    for index, song in enumerate(results):
        formatted_result = formatted_result + f"""
{index+1}. {song["title"]} _by_ {song["artists"][0]["name"]}
_Link:_ https://music.youtube.com/watch?v={song["videoId"]}
"""
    return formatted_result


def yt_download_song(link: str):
    # ytmusic.get_song(link)
    mk_base()
    download_audio([link])

@st.dialog("YTDownloader")
def handle_download_dialog():
    st.write("YouTube Link")
    link_input = st.text_input(label="Link")
    download_button = st.button("Download", key="handle_download")
    if bool(link_input) and download_button:
        with st.spinner("Downloading...", show_time=True):
            yt_download_song(link_input)
            st.toast("Downloaded")
        time.sleep(3)
        st.rerun()
    else:
        st.error("Please provide a YouTube Link")

if "yt_link" not in st.session_state:
    st.write("Search or Download")
    if st.button("Search"):
        st.toast("hol' up")
    if st.button("Download"):
        handle_download_dialog()
else:
    st.write("")

# >>> import streamlit as st
# >>>
# >>> @st.dialog("Cast your vote")
# >>> def vote(item):
# >>>     st.write(f"Why is {item} your favorite?")
# >>>     reason = st.text_input("Because...")
# >>>     if st.button("Submit"):
# >>>         st.session_state.vote = {"item": item, "reason": reason}
# >>>         st.rerun()
# >>>
# >>> if "vote" not in st.session_state:
# >>>     st.write("Vote for your favorite")
# >>>     if st.button("A"):
# >>>         vote("A")
# >>>     if st.button("B"):
# >>>         vote("B")
# >>> else:
# >>>     f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"