import streamlit as st

from home_page import abstract
from music_page import music
from info_page import info

def main():
    
    st.title("🎹 Music Generator using Deep Learning 🎹")
    page = side_bar()
    if page == "Home":
        abstract()
    elif page == "Model Info":
        info()
    else:
        music()

def side_bar():
    with st.sidebar:

        st.title("Music Generation Project")
        st.header("Navigate between pages-")

        page = st.radio("GoTo", ("Home", "Model Info", "Generate Music"))
    
    return page

if __name__ == "__main__":
    st.set_page_config(page_title="Music Generator", page_icon="✨")
    main()
