import click
import pandas as pd
import numpy as np
import soundfile as sf
from pathlib import PurePath
import buschwerkzeug as bw
import pickle
import tensorflow as tf
import math

from .config import config
fs = config['sampling_rate']
stft_len = config['cnn']['stft_len']
stft_hop = config['cnn']['stft_hop']
win_len = config['cnn']['win_len']
n_freq = stft_len//2

import sys
import os
is_frozen = getattr(sys, 'frozen', False)

if is_frozen:
    model_dir = getattr(sys, '_MEIPASS', '')
else:
    model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model')
model_file = os.path.join(model_dir, 'cnn')

os.environ["CUDA_VISIBLE_DEVICES"]="-1"

@click.command()
@click.argument('files', type=click.Path(True), nargs=-1)
@click.argument('out_table', type=click.Path())
@click.option('--prob-dir', type=click.Path(True))
def main(files, out_table, prob_dir):
    """ 
    """

    r = pd.DataFrame()

    for fname in files:
        print('Predicting', fname)
        segments, Y = predict(fname)
        r = r.append(segments)
        if prob_dir:
            outfile = '{}/{}.npy'.format(prob_dir, PurePath(fname).name)
            with open(outfile, 'wb') as out:
                np.save(out, Y)
    r.to_csv(out_table)


def predict(fname):
    if not hasattr(predict, 'model'):
        predict.model = tf.keras.models.load_model(model_file)
    if not hasattr(predict, 'scaler'):
        with open(model_file + '.scaler', 'rb') as f:
            predict.scaler = pickle.load(f)
    wav, fs = sf.read(fname)
    f,t,S = bw.signal.spectrogram(wav, fs, stft_len, stft_len-stft_hop)
    S = S.T
    n = math.ceil(len(S)/win_len)
    S = np.pad(S, ((0,(-len(S))%win_len), (0,0)))
    X = np.array(np.split(np.array(S[:,:, None]),n))
    X = predict.scaler.transform(X)
    Y = np.concatenate(predict.model.predict(X)).flatten()
    segments = bw.segments.segments(Y, hold_len = 0.03*fs/stft_hop, min_len = 0.03*fs/stft_hop, threshold_method = 0.5)
    if not segments.empty:
        def d(r):
            return f[int(np.median(np.argmax(S[r.start:r.end,:], axis=1)))]
        dominant_freq = segments.aggregate(d, axis=1)
        segments['freq_low'] = dominant_freq - 50
        segments['freq_high'] = dominant_freq + 50
        segments.start = (segments.start*stft_hop).astype(int)
        segments.end = (segments.end*stft_hop).astype(int)
        segments = bw.segments.consecutive(segments, max_gap = 1*fs)
        segments['fname'] = PurePath(fname).name
    return segments, Y






