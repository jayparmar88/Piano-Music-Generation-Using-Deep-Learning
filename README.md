# Piano Music Generation using Deep Learning :

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Model Architecture](#model-architecture)
- [License](#license)

## Project Overview :

In recent years, recurrent neural network models have defined the normative process in producing efficient and reliable results in various challenging problems such as translation, voice recognition and 
image captioning, thereby making huge strides in learning useful feature representations. With these latest advancements in deep learning, RNNs have garnered fame in computational creativity tasks such as 
even that of music generation. In this project, simple piano tunes are used for training and generating new music using deep learning.

## Music Data :

To initiate the music generation process, the model is trained on input music data, primarily in the form of MIDI files. The data is categorized into two main object types: notes and chords. 
Note objects encapsulate information about pitch, octave, and offset, while Chord objects act as containers for a set of notes played simultaneously. The pitch is represented by the letters A-G, 
denoting the frequency of the sound, while the octave signifies the pitch set on a piano. Offset denotes the position of the note in the piece.

## Model :

LSTM (Long Short-Term Memory) is a type of recurrent neural network (RNN) that is particularly effective at processing sequential data such as audio, speech, and music. Music is a form of sequential data 
because it has a temporal structure: notes are played one after the other, and there is often a rhythmic pattern.

LSTM models are particularly useful for music generation because they can learn to capture long-term dependencies between notes and chords, which is important for creating music that sounds coherent and 
musically pleasing. Traditional feedforward neural networks struggle with processing sequential data because they don't have any memory of past inputs. LSTMs, on the other hand, have a built-in memory mechanism 
that allows them to keep track of past inputs and use that information to inform future predictions.

In music generation using deep learning, the LSTM model is typically trained on a large dataset of existing music to learn the patterns and structure of music. Once the model is trained, it can be used 
to generate new music by sampling from the learned distribution of notes and chords. By adjusting the temperature parameter of the sampling process, the model can be made more or less creative, 
producing variations on the learned patterns or generating entirely new musical ideas.

## Features :

- **Piano Music Generation:** The primary feature is the ability to generate piano music using a pre-trained deep learning model.
- **Customization:** Users can tweak various parameters to influence the style, tempo, and complexity of the generated music.
- **Evaluation:** Assess the quality of generated music using metrics like melody coherence, harmony, and overall composition structure.

## Requirements :

- python
- streamlit
- scipy
- keras
- numpy
- music21
- pretty_midi
- tensorflow
- tensorflow-cpu
- f fluidsynth-2.3.2.tar.gz

## Installation :

1. Clone the repository:

```bash
git clone https://github.com/jayparmar88/Music-Generation.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Model Architecture :

Our model incorporates four main types of layers:

- **LSTM Layers:** Recurrent Neural Net layers that process sequences and can return sequences or matrices.
- **Dropout Layers:** Regularization technique to prevent overfitting by randomly setting a fraction of input units to zero during training.
- **Dense Layers:** Fully connected neural network layers where each input node is connected to each output node.
- **Activation Layers:** Determine the activation function for calculating the output of a node.

For each LSTM, Dense, and Activation layer, the first parameter specifies the number of nodes in the layer. For the Dropout layer, the first parameter indicates the fraction of input units to be dropped during training

The model architecture used in this project is shown below.

![Model Architecture](https://github.com/jayparmar88/Music-Generation/blob/main/img/Model_Architecture.png)

## Web App :

I have deployed web-app for this project using streamlit platform.
![Project link](https://jayparmar88-music-generation-app-jqlji9.streamlit.app/)

## License :

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
