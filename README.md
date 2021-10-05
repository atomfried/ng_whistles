# NG whistle detector

## Project description
A python module / standalone executable that detects flat whistles in nightingale song using a tensorflow CRNN model.

## Getting Started

### Prerequisites
* python 3
* pip
* A GPU is NOT required.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/atomfried/ng_whistles.git
   ```
2. Install the module and it's requirements
   ```sh
   cd ng_whistles
   pip3 install .
   ```

### Usage
The *example* directory contains some wavs with nightingale song. Detect whistle segments like so:
```sh
python3 -m ng_whistles examples/*.wav whistles.csv
```
The created  table `whistles.csv` contains one line per detected whistle, specifying file name, start and end time (in samples), and frequency range (in Hz).


### Standalone
Build a standalone executable like so:
   ```sh
   pip3 install pyinstaller
   make
   ```
The executable file is created in the directory `dist`.
If you're building in a virtualenv, missing module issues might be fixed by using
   ```sh
   make with_virtualenv
   ```
   instead.
   
## About the model

### Architecture
Whistle probability is predicted via a Convolutional Recurrent Neuronal Network (CRNN) implemented in tensorflow. The model input, a spectrogram segment, is run through three convoluted layers, two recurrent layes and one fully connected layers, reducing the features space along to frequency axis to a single value while preserving resolution along the time axis. Model output are class (i.e. whistle) probabilites for each spectrogram time frame. This architecture was first proposed in https://doi.org/10.1109/TASLP.2017.2690575.

### Training data
TODO

## Contact
coder@posteo.de

