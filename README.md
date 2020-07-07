# An electrodiffusive neuron-extracellular-glia model with somatodendritic interactions

This code was used to produce the results presented in Sætra et al. 2020: An electrodiffusive neuron-extracellular-glia model with somatodendritic interactions (bioRxiv).

# Installation

To install the code, clone or download the repo, navigate to the top directory of the repo and enter the following command
in the terminal: 
```bash
python setup.py install
```

You must have edNEGmodel and PRmodel installed. They can be downloaded from 
[https://github.com/CINPLA/edNEGmodel](https://github.com/CINPLA/edNEGmodel) and [https://github.com/CINPLA/PRmodel](https://github.com/CINPLA/PRmodel), respectively.

The code was run with Ubuntu 18.04.3 and Python 3.6.9.

# Reproducing the results of the paper

To reproduce the results of the paper,
run `bash run_all.sh`. Note that this might run for a couple of days on a normal computer. To plot and save the figures, run 
`bash plot_all.sh` from the folder named figures.

If you have problems reading the initial_values.npz-file, install git lfs and try `git-lfs pull`.
