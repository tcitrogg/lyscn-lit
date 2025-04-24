import streamlit as st
from ytmusicapi import YTMusic

ytmusic = YTMusic()

METAINFO = {
    "title": "Lyscn",
    "icon": "🌊",
    "dir": "/audio"
}

def handle_music_search(query: str):
    results = ytmusic.search(query, filter="songs", limit=100)
    formatted_result = ""
    for index, song in enumerate(results):
        formatted_result = formatted_result + f"""
{index+1}. {song["title"]} _by_ {song["artists"][0]["name"]}
_Link:_ https://music.youtube.com/watch?v={song["videoId"]}
"""

    return formatted_result


# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []
    
    
# Display chat history from history on app rerun
for history in st.session_state.history:
    with st.chat_message(history["role"], avatar=history["avatar"]):
        st.markdown(history["content"])

if userinput := st.chat_input("Search 'Dizzyeight'"):    
    
    # Display user history in chat history container
    st.chat_message("user", avatar="😃").markdown(userinput)
    # Add user history to chat history
    st.session_state.history.append({"role": "user", "avatar":"😃", "content": userinput})
    
    with st.spinner("Loading..."):
        response = handle_music_search(userinput)
        # Display assistant response in chat history container
        lyscn_input = st.chat_message(METAINFO["title"], avatar=METAINFO["icon"])
    with lyscn_input:
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.history.append({"role": METAINFO["title"], "avatar":METAINFO["icon"], "content": response})