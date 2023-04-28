import streamlit as st

def info():

    st.header("Model")

    st.write("In our model we use four different types of layers:")
   
    st.markdown("<ol>\
                <li>LSTM layers is a Recurrent Neural Net layer that takes a sequence as an input and can return either sequences (return_sequences=True) or a matrix.</li>\
                <li>Dropout layers are a regularisation technique that consists of setting a fraction of input units to 0 at each update during the training to prevent overfitting. The fraction is determined by the parameter used with the layer.</li>\
                <li>Dense layers or fully connected layers is a fully connected neural network layer where each input node is connected to each output node.</li>\
                <li>The Activation layer determines what activation function our neural network will use to calculate the output of a node./li>\
                </ol>", unsafe_allow_html = True)

    st.write("For each LSTM, Dense, and Activation layer the first parameter is how many nodes the layer should have. For the Dropout \
    layer the first parameter is the fraction of input units that should be dropped during training. For each LSTM, Dense, and \
    Activation layer the first parameter is how many nodes the layer should have. For the Dropout layer the first parameter is the \
    fraction of input units that should be dropped during training.")
    
    st.subheader("🌉 Model Architechture")
    st.image("./src/assets/img/Model_Architechture.png")

    st.markdown('---')
    st.caption("made by Jay Parmar")
