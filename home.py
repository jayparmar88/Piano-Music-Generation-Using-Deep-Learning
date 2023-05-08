import streamlit as st

def abstract():
    st.image("https://www.taylorintime.com/wp-content/uploads/2016/11/Music-980x613.jpg")

    st.header("Abstract")
    st.write("In recent years, recurrent neural network models have defined the normative process \
    in producing efficient and reliable results in various challenging problems such as translation, \
    voice recognition and image captioning, thereby making huge strides in learning useful feature representations. \
    With these latest advancements in deep learning, RNNs have garnered fame in computational creativity \
    tasks such as even that of music generation. In this project, simple piano tunes are used for training \
    and generating new music using deep learning.")
    
    st.subheader("Music data")
    st.write("For generating music, first we have to train model using input music data. for \
    the input data we are passing midi files. The data splits into two  object types: notes and chords. \
    Note objects contain information about the pitch, octave, and offset of the Note. \
    Pitch refers to the frequency of the sound, or how high or low it is and is represented with the letters [A, B, C, D, E, F, G], with A being \
    the highest and G being the lowest. Octave refers to which set of pitches you use on a piano. \
    Offset refers to where the note is located in the piece. And Chord objects are essentially a container for a set of notes that are played at the same time.")
    
    st.markdown('---')
    
    st.header("Model")
    
    st.subheader("Why lstm model is used in this project")
    st.write("LSTM (Long Short-Term Memory) is a type of recurrent neural network (RNN) that is particularly effective \
    at processing sequential data such as audio, speech, and music. Music is a form of sequential data because it has a \
    temporal structure: notes are played one after the other, and there is often a rhythmic pattern.")

    st.write("LSTM models are particularly useful for music generation because they can learn to capture long-term dependencies \
    between notes and chords, which is important for creating music that sounds coherent and musically pleasing. \
    Traditional feedforward neural networks struggle with processing sequential data because they don't have any memory of past inputs. \
    LSTMs, on the other hand, have a built-in memory mechanism that allows them to keep track of past inputs and use that information \
    to inform future predictions.")

    st.write("In music generation using deep learning, the LSTM model is typically trained on a large dataset of existing music to learn the \
    patterns and structure of music. Once the model is trained, it can be used to generate new music by sampling from the learned \
    distribution of notes and chords. By adjusting the temperature parameter of the sampling process, the model can be made more or \
    less creative, producing variations on the learned patterns or generating entirely new musical ideas.")

    st.subheader("Our Model")
    st.write("In our model we use four different types of layers:")
   
    st.markdown("<ol>\
                <li>LSTM layers is a Recurrent Neural Net layer that takes a sequence as an input and can return either sequences (return_sequences=True) or a matrix.</li>\
                <li>Dropout layers are a regularisation technique that consists of setting a fraction of input units to 0 at each update during the training to prevent overfitting. The fraction is determined by the parameter used with the layer.</li>\
                <li>Dense layers or fully connected layers is a fully connected neural network layer where each input node is connected to each output node.</li>\
                <li>The Activation layer determines what activation function our neural network will use to calculate the output of a node.</li>\
                </ol>", unsafe_allow_html = True)

    st.write("For each LSTM, Dense, and Activation layer the first parameter is how many nodes the layer should have. For the Dropout \
    layer the first parameter is the fraction of input units that should be dropped during training.")
    
    st.subheader("🌉 Model Architecture")
    st.image("./img/Model_Architecture.png")

    st.markdown('---')

    st.caption("made by Jay Parmar")
