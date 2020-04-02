# This script takes the structure of the experiment provided by the
# StimuliTable-Encoding and StimuliTable-Recognition, and creates a specified
# number of stimuli tables with the images selected randomly.

import pandas as pd
import trk_module as trk
import os.path as op

n_files = 2 # define number of stimuli files to be created
encoding_fname = 'StimuliTable-Encoding_3-runs_40-pairs_8-discrete-loc_12345-delays.xlsx'
recognition_fname = 'StimTable-Recognition.xlsx'
encoding_table = pd.read_excel(encoding_fname)
recognition_table = pd.read_excel(recognition_fname)

for i in range(n_files):
    outpath = 'stimuli_tables'
    encoding_trials_fname = 'encoding_trials_{}.csv'.format(str(i))
    regognition_trials_fname = 'recognition_trials_{}.csv'.format(str(i))
    encoding_trials = trk.set_encoding_trials(encoding_table, 121, 145)
    encoding_trials.to_csv(op.join(outpath, encoding_trials_fname), index=False)
