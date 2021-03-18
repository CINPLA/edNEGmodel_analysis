import numpy as np
import matplotlib.pyplot as plt

def mean_phi(filename, t_thresh):
    """
    Read t, syn_rate, phi_se_n, phi_se_g, and phi_se_diff from file 
    and calculate the average value of the different phi components 
    taken over the last (t - t_thresh) seconds of the simulations.
    """

    syn_rate = []
    mean_phi_e_n = []
    mean_phi_e_g = []
    mean_phi_e_diff = []

    for k in range(1,5):
        data = np.load(filename + str(k) + '.npz')

        t = data['t']
        phi_e_n = data['phi_e_n']
        phi_e_g = data['phi_e_g']
        phi_e_diff = data['phi_e_diff']
        syn_rate_ = data['syn_rate']
        
        N = 0
        mean_phi_e_n_ = 0
        mean_phi_e_g_ = 0
        mean_phi_e_diff_ = 0
        for i in range(len(t)-1):
            if t[i] > t_thresh:
                mean_phi_e_n_ += phi_e_n[i]
                mean_phi_e_g_ += phi_e_g[i]
                mean_phi_e_diff_ += phi_e_diff[i]
                N += 1
        mean_phi_e_n_ = mean_phi_e_n_/N*1000
        mean_phi_e_g_ = mean_phi_e_g_/N*1000
        mean_phi_e_diff_ = mean_phi_e_diff_/N*1000
        
        syn_rate.append(syn_rate_)
        mean_phi_e_n.append(mean_phi_e_n_)
        mean_phi_e_g.append(mean_phi_e_g_)
        mean_phi_e_diff.append(mean_phi_e_diff_)

    return syn_rate, mean_phi_e_n, mean_phi_e_g, mean_phi_e_diff


t_thresh = 50
syn_rate_soma_ss, n_soma_ss, g_soma_ss, diff_soma_ss = mean_phi('data/figure7_syn_soma_ss_', t_thresh)
syn_rate_dendrite_ss, n_dendrite_ss, g_dendrite_ss, diff_dendrite_ss = mean_phi('data/figure7_syn_dendrite_ss_', t_thresh)
syn_rate_both_ss, n_both_ss, g_both_ss, diff_both_ss = mean_phi('data/figure7_syn_both_ss_', t_thresh)

t_thresh = 590
syn_rate_soma_db, n_soma_db, g_soma_db, diff_soma_db = mean_phi('data/figure7_syn_soma_db_', t_thresh)
syn_rate_dendrite_db, n_dendrite_db, g_dendrite_db, diff_dendrite_db = mean_phi('data/figure7_syn_dendrite_db_', t_thresh)
syn_rate_both_db, n_both_db, g_both_db, diff_both_db = mean_phi('data/figure7_syn_both_db_', t_thresh)

np.savez('data/figure7.npz', \
syn_rate_soma_ss=syn_rate_soma_ss, \
n_soma_ss=n_soma_ss, \
g_soma_ss=g_soma_ss, \
diff_soma_ss=diff_soma_ss, \
syn_rate_dendrite_ss=syn_rate_dendrite_ss, \
n_dendrite_ss=n_dendrite_ss, \
g_dendrite_ss=g_dendrite_ss, \
diff_dendrite_ss=diff_dendrite_ss, \
syn_rate_both_ss=syn_rate_both_ss, \
n_both_ss=n_both_ss, \
g_both_ss=g_both_ss, \
diff_both_ss=diff_both_ss, \
syn_rate_soma_db=syn_rate_soma_db, \
n_soma_db=n_soma_db, \
g_soma_db=g_soma_db, \
diff_soma_db=diff_soma_db, \
syn_rate_dendrite_db=syn_rate_dendrite_db, \
n_dendrite_db=n_dendrite_db, \
g_dendrite_db=g_dendrite_db, \
diff_dendrite_db=diff_dendrite_db, \
syn_rate_both_db=syn_rate_both_db, \
n_both_db=n_both_db, \
g_both_db=g_both_db, \
diff_both_db=diff_both_db)
