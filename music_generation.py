import streamlit as st

def music():
    
    st.header("🎵 Audio samples to train model")

    col1, col2 = st.columns(2)
    st.markdown('---')
    col3, col4 = st.columns(2)

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

        st.markdown("<b> Option 1:</b> <br>Classical Music by **Chopin**:", unsafe_allow_html=True)
        st.caption("chopin 1")
        st.audio(st.session_state["chopin1"], format='audio/mp3')
        st.caption("chopin 2")
        st.audio(st.session_state["chopin2"], format='audio/mp3')
        st.caption("chopin 3")
        st.audio(st.session_state["chopin3"], format='audio/mp3')

    with col2:
        midi_file1 = open("./music_samples/borodin/bor_ps1.mid", 'rb')
        midi_file2 = open("./music_samples/borodin/bor_ps4.mid", 'rb')
        midi_file3 = open("./music_samples/borodin/bor_ps6.mid", 'rb')
        try:
            if "borodin1" not in st.session_state:
                st.session_state["borodin1"] = convert_midi_to_wav(midi_file1)
            if "borodin2" not in st.session_state:
                st.session_state["borodin2"] = convert_midi_to_wav(midi_file2)
            if "borodin3" not in st.session_state:
                st.session_state["borodin3"] = convert_midi_to_wav(midi_file3)
        except Exception as e:
            if "borodin1" not in st.session_state:
                st.session_state["borodin1"] = open("./music_samples/mp3_versions/bor_ps1.mp3", 'rb').read()
            if "borodin2" not in st.session_state:
                st.session_state["borodin2"] = open("./music_samples/mp3_versions/bor_ps4.mp3", 'rb').read()
            if "borodin3" not in st.session_state:
                st.session_state["borodin3"] = open("./music_samples/mp3_versions//bor_ps6.mp3", 'rb').read()

        st.markdown("<b> Option 2:</b> <br>Classical Music by **Borodin**:", unsafe_allow_html=True)
        st.caption("borodin 1")
        st.audio(st.session_state["borodin1"], format='audio/mp3')
        st.caption("borodin 2")
        st.audio(st.session_state["borodin2"], format='audio/mp3')
        st.caption("borodin 3")
        st.audio(st.session_state["borodin3"], format='audio/mp3')
        
    with col3:
        midi_file1 = open("./music_samples/haydn/hay_40_1.mid", 'rb')
        midi_file2 = open("./music_samples/haydn/haydn_35_3.mid", 'rb')
        midi_file3 = open("./music_samples/haydn/haydn_8_2.mid", 'rb')
        try:
            if "haydn1" not in st.session_state:
                st.session_state["haydn1"] = convert_midi_to_wav(midi_file1)
            if "haydn2" not in st.session_state:
                st.session_state["haydn2"] = convert_midi_to_wav(midi_file2)
            if "haydn3" not in st.session_state:
                st.session_state["haydn3"] = convert_midi_to_wav(midi_file3)
        except Exception as e:
            if "haydn1" not in st.session_state:
                st.session_state["haydn1"] = open("./music_samples/mp3_versions/hay_40_1.mp3", 'rb').read()
            if "haydn2" not in st.session_state:
                st.session_state["haydn2"] = open("./music_samples/mp3_versions/haydn_35_3.mp3", 'rb').read()
            if "haydn3" not in st.session_state:
                st.session_state["haydn3"] = open("./music_samples/mp3_versions/haydn_8_2.mp3", 'rb').read()

        st.markdown("<b> Option 3:</b> <br>Classical Music by **Haydn**:", unsafe_allow_html=True)
        st.caption("haydn 1")
        st.audio(st.session_state["haydn1"], format='audio/mp3')
        st.caption("haydn 2")
        st.audio(st.session_state["haydn2"], format='audio/mp3')
        st.caption("haydn 3")
        st.audio(st.session_state["haydn3"], format='audio/mp3')
        
    with col4:
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
        
        st.markdown("<b> Option 4:</b> <br>Classical Music by **Hybrid**:", unsafe_allow_html=True)
        st.caption("hybrid 1")
        st.audio(st.session_state["hybrid1"], format='audio/mp3')
        st.caption("hybrid 2")
        st.audio(st.session_state["hybrid2"], format='audio/mp3')
        st.caption("hybrid 3")
        st.audio(st.session_state["hybrid3"], format='audio/mp3')
    
    st.markdown('---')

    with st.form("Batch Selection"):
        st.subheader("Choose a style of music to generate synthetic version:")
        batch = st.radio('Style', options=("Chopin Music", "Borodin Music", "Haydn Music", "Hybrid Music"))
        confirm = st.form_submit_button("Generate Music")

    if confirm:
        if batch == "Chopin Music":
            with st.spinner("Generating Chopin Music"):
                with st.empty():
                
                        try:
                            output = convert_midi_to_wav(open("./music_samples/mp3_versions/test_output_chopin.mid", 'rb'))
                        except Exception as e:
                            output = open("./music_samples/mp3_versions/test_output_chopin.mp3", 'rb').read()
                st.snow()  
            
            # st.caption(c)
            st.subheader("🎉 Sample music generated : (Chopin Music)")
            st.audio(output, format="mp3")
            
        if batch == "Borodin Music":
            with st.spinner("Generating Borodin Music"):
                with st.empty():
                
                        try:
                            output = convert_midi_to_wav(open("./music_samples/mp3_versions/test_output_borodin.mid", 'rb'))
                        except Exception as e:
                            output = open("./music_samples/mp3_versions/test_output_borodin.mp3", 'rb').read()
                st.balloon()
                
            # st.caption(c)
            st.subheader("🎉 Sample music generated : (Borodin Music)")
            st.audio(output, format="wav")
                        
        if batch == "Haydn Music":
            with st.spinner("Generating Haydn Music"):
                with st.empty():
                
                        try:
                            output = convert_midi_to_wav(open("./music_samples/mp3_versions/test_output_haydn.mid", 'rb'))
                        except Exception as e:
                            output = open("./music_samples/mp3_versions/test_output_haydn.mp3", 'rb').read()
                st.snow() 
                
            # st.caption(c)
            st.subheader("🎉 Sample music generated : (Haydn Music)")
            st.audio(output, format="wav")
                        
        if batch == "Hybrid Music":
            with st.spinner("Generating Hybrid Music"):
                with st.empty():

                        try:
                            output = convert_midi_to_wav(open("./music_samples/mp3_versions/test_output_hybrid.mid", 'rb'))
                        except Exception as e:
                            output = open("./music_samples/mp3_versions/test_output_hybrid.mp3", 'rb').read()
                            
                st.snow() 
                            
            # st.caption(c)
            st.subheader("🎉 Sample music generated : (Hybrid Music)")
            st.audio(output, format="wav")
            
    st.markdown('---')
    st.subheader("Music tune generated using Pokemon music files")
    st.write("For more example, I used so many pokemon piano tunes to train this model and it generate this tune using this model.")
    st.image("https://media.tenor.com/hzVy-nB15DoAAAAi/music-pokemon.gif", width=88)
    with st.columns(2)[0]:
        st.audio(open("./music_samples/Pokemon_output.mp3", 'rb').read(), format='audio/mp3')
    
    st.markdown('---')
    st.caption("made by Jay Parmar")
