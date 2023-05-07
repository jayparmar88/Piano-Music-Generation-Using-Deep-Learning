import streamlit as st

from home import abstract
from music_generation import music

def main():
    
    st.title("🎹 Music Generation using Deep Learning")
    page = side_bar()
    if page == "Home":
        abstract()
    else:
        music()

def side_bar():
    with st.sidebar:

        st.title("Music Generation Project")

        page = st.radio("GoTo", ("Home", "Music_Generate"))
    
    return page

if __name__ == "__main__":
    st.set_page_config(page_title="Music Generation", page_icon="✨")
    main()
