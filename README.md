# An electrodiffusive neuron-extracellular-glia model for exploring the genesis of slow potentials in the brain 

This code was used to produce the results presented in Sætra et al. 202X: 

# Installation

To install the code, clone or download the repo, navigate to the top directory of the repo and enter the following command
in the terminal: 
```bash
python setup.py install
```

You must have edNEGmodel installed, which can be downloaded from 
[https://github.com/CINPLA/edNEGmodel](https://github.com/CINPLA/edNEGmodel).

The code was run with Ubuntu 18.04.3 and Python 3.6.9.

# Reproducing the results of the paper

To reproduce the results of the paper,
run `bash run_all.sh`. Note that this might run for several days on a normal computer. To plot and save the figures, run 
`bash plot_all.sh` from the folder named figures.

If you have problems reading the initial_values.npz-file, install git lfs and try `git-lfs pull`.
