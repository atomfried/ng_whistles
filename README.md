# NG whistle detector

## Synopsis
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

## Contact
coder@posteo.de

