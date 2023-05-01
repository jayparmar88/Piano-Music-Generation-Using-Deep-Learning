import streamlit as st

def music():
    
    st.header("🎵 Audio samples to train model")

    col1, col2, col3, col4 = st.columns(4)

    if "classical" not in st.session_state:
        st.session_state["classical"] = True
    if "concert" not in st.session_state:
        st.session_state["concert"] = True

    with col1:
        midi_file1 = open("./music_samples/chopin/chpn-p11.mid", 'rb')
        midi_file2 = open("./music_samples/chopin/chpn_op23.mid", 'rb')
        midi_file3 = open("./music_samples/chopin/chpn_op7_1.mid", 'rb')
        try:
            if "chopin1" not in st.session_state:
                st.session_state["chopin1"] = convert_midi_to_wav(midi_file1)
            if "chopin2" not in st.session_state:
                st.session_state["chopin2"] = convert_midi_to_wav(midi_file2)
            if "chopin3" not in st.session_state:
                st.session_state["chopin3"] = convert_midi_to_wav(midi_file3)
        except Exception as e:
            if "chopin1" not in st.session_state:
                st.session_state["chopin1"] = open("./music_samples/mp3_versions/chpn-p11.mp3", 'rb').read()
            if "chopin2" not in st.session_state:
                st.session_state["chopin2"] = open("./music_samples/mp3_versions/chpn_op23.mp3", 'rb').read()
            if "chopin3" not in st.session_state:
                st.session_state["chopin3"] = open("./music_samples/mp3_versions/chpn_op7_1.mp3", 'rb').read()

        st.markdown("<b> Option 1:</b> <br>Classical Music by  **Chopin**:", unsafe_allow_html=True)
        st.caption("chopin 1")
        st.audio(st.session_state["chopin1"], format='audio/mp3')
        st.caption("chopin 2")
        st.audio(st.session_state["chopin2"], format='audio/mp3')
        st.caption("chopin 3")
        st.audio(st.session_state["chopin3"], format='audio/mp3')


    with col2:
        midi_file4 = open("./music_samples/hybrid/BlueStone_LastDungeon.mid", 'rb')
        midi_file5 = open("./music_samples/hybrid/cosmo.mid", 'rb')
        midi_file6 = open("./music_samples/hybrid/figaro.mid", 'rb')
        try:
            if "hybrid1" not in st.session_state:
                st.session_state["hybrid1"] = convert_midi_to_wav(midi_file4)
            if "hybrid2" not in st.session_state:
                st.session_state["hybrid2"] = convert_midi_to_wav(midi_file5)
            if "hybrid3" not in st.session_state:
                st.session_state["hybrid3"] = convert_midi_to_wav(midi_file6)
        except Exception as e:
            if "hybrid1" not in st.session_state:
                st.session_state["hybrid1"] = open("./music_samples/mp3_versions/BlueStone_LastDungeon.mp3", 'rb').read()
            if "hybrid2" not in st.session_state:
                st.session_state["hybrid2"] = open("./music_samples/mp3_versions/cosmo.mp3", 'rb').read()
            if "hybrid3" not in st.session_state:
                st.session_state["hybrid3"] = open("./music_samples/mp3_versions/figaro.mp3", 'rb').read()
        
        st.markdown("<b> Option 2:</b> <br>Classical Music  **Hybrid**:", unsafe_allow_html=True)
        st.caption("hybrid 1")
        st.audio(st.session_state["hybrid1"], format='audio/mp3')
        st.caption("hybrid 2")
        st.audio(st.session_state["hybrid2"], format='audio/mp3')
        st.caption("hybrid 3")
        st.audio(st.session_state["hybrid3"], format='audio/mp3')
        
     with col3:
        midi_file1 = open("./music_samples/albeniz/alb_esp1.mid", 'rb')
        midi_file2 = open("./music_samples/albeniz/alb_esp4.mid", 'rb')
        midi_file3 = open("./music_samples/albeniz/alb_se8.mid", 'rb')
        try:
            if "albeniz1" not in st.session_state:
                st.session_state["albeniz1"] = convert_midi_to_wav(midi_file1)
            if "albeniz2" not in st.session_state:
                st.session_state["albeniz2"] = convert_midi_to_wav(midi_file2)
            if "albeniz3" not in st.session_state:
                st.session_state["albeniz3"] = convert_midi_to_wav(midi_file3)
        except Exception as e:
            if "albeniz1" not in st.session_state:
                st.session_state["albeniz1"] = open("./music_samples/mp3_versions/alb_esp1.mp3", 'rb').read()
            if "albeniz2" not in st.session_state:
                st.session_state["albeniz2"] = open("./music_samples/mp3_versions/alb_esp4.mp3", 'rb').read()
            if "albeniz3" not in st.session_state:
                st.session_state["albeniz3"] = open("./music_samples/mp3_versions//alb_se8.mp3", 'rb').read()

        st.markdown("<b> Option 1:</b> <br>Classical Music by  **albeniz**:", unsafe_allow_html=True)
        st.caption("albeniz 1")
        st.audio(st.session_state["albeniz1"], format='audio/mp3')
        st.caption("albeniz 2")
        st.audio(st.session_state["albeniz2"], format='audio/mp3')
        st.caption("albeniz 3")
        st.audio(st.session_state["albeniz3"], format='audio/mp3')
        
     with col4:
        midi_file1 = open("./music_samples/albeniz/alb_esp1.mid", 'rb')
        midi_file2 = open("./music_samples/albeniz/alb_esp4.mid", 'rb')
        midi_file3 = open("./music_samples/albeniz/alb_se8.mid", 'rb')
        try:
            if "albeniz1" not in st.session_state:
                st.session_state["albeniz1"] = convert_midi_to_wav(midi_file1)
            if "albeniz2" not in st.session_state:
                st.session_state["albeniz2"] = convert_midi_to_wav(midi_file2)
            if "albeniz3" not in st.session_state:
                st.session_state["albeniz3"] = convert_midi_to_wav(midi_file3)
        except Exception as e:
            if "albeniz1" not in st.session_state:
                st.session_state["albeniz1"] = open("./music_samples/mp3_versions/alb_esp1.mp3", 'rb').read()
            if "albeniz2" not in st.session_state:
                st.session_state["albeniz2"] = open("./music_samples/mp3_versions/alb_esp4.mp3", 'rb').read()
            if "albeniz3" not in st.session_state:
                st.session_state["albeniz3"] = open("./music_samples/mp3_versions//alb_se8.mp3", 'rb').read()

        st.markdown("<b> Option 1:</b> <br>Classical Music by  **albeniz**:", unsafe_allow_html=True)
        st.caption("albeniz 1")
        st.audio(st.session_state["albeniz1"], format='audio/mp3')
        st.caption("albeniz 2")
        st.audio(st.session_state["albeniz2"], format='audio/mp3')
        st.caption("albeniz 3")
        st.audio(st.session_state["albeniz3"], format='audio/mp3')
    
    st.markdown('---')

    with st.form("Batch Selection"):
        st.subheader("Choose a style of music to generate synthetic version:")
        batch = st.radio('Style', options=("Chopin Music", "Hybrid Music"))
        confirm = st.form_submit_button("Generate Music")

    if confirm:
        if batch == "Chopin Music":
            with st.spinner("Generating Chopin Music"):
                with st.empty():
                    
                    if st.session_state["classical"]:
                        c = "chopin"
                        try:
                            output = convert_midi_to_wav(open("./music_samples/mp3_versions/test_output_chopin.mid", 'rb'))
                        except Exception as e:
                            output = open("./music_samples/mp3_versions/test_output_chopin.mp3", 'rb').read()
                        st.session_state["classical"] = False
                    else:
                        c = "borodin"
                        try:
                            output = convert_midi_to_wav(open("./music_samples/mp3_versions/test_output_borodin.mid", 'rb'))
                        except Exception as e:
                            output = open("./music_samples/mp3_versions/test_output_borodin.mp3", 'rb').read()
                        st.session_state["classical"] = True
            # st.caption(c)
            st.subheader("🎉 Sample music generated : (Chopin Music)")
            st.audio(output, format="mp3")

        if batch == "Hybrid Music":
            with st.spinner("Generating Hybrid Music"):
                with st.empty():
                    
                    if st.session_state["concert"]:
                        c = "best"
                        try:
                            output = convert_midi_to_wav(open("./music_samples/mp3_versions/test_output_best.mid", 'rb'))
                        except Exception as e:
                            output = open("./music_samples/mp3_versions/test_output_best.mp3", 'rb').read()
                        st.session_state["concert"] = False
                    else:
                        c = "better"
                        try:
                            output = convert_midi_to_wav(open("./music_samples/mp3_versions/test_output_better.mid", 'rb'))
                        except Exception as e:
                            output = open("./music_samples/mp3_versions/test_output_better.mp3", 'rb').read()
                        st.session_state["concert"] = True
                    
            # st.caption(c)
            st.subheader("🎉 Sample music generated : (Hybrid)")
            st.audio(output, format="wav")
            
    st.subheader("Pokemon music tune generated by this model")
    st.write("For more example, I gave so many pokemon piano tune to this model for training and it generate this tune using this model.")
    st.image("https://media.tenor.com/hzVy-nB15DoAAAAi/music-pokemon.gif")
    with st.columns(2)[0]:
        st.audio(open("./music_samples/Pokemon_output.mp3", 'rb').read(), format='audio/mp3')
    
    st.markdown('---')
    st.caption("made by Jay Parmar")
