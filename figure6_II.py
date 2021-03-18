import numpy as np
import matplotlib.pyplot as plt

def mean_phi(filename, t_thresh):
    """
    Read t, I_stim, phi_se_n, phi_se_g, and phi_se_diff from file 
    and calculate the average value of the different phi components 
    taken over the last (t - t_thresh) seconds of the simulations.
    """

    I_stim = []
    mean_phi_e_n = []
    mean_phi_e_g = []
    mean_phi_e_diff = []

    for k in range(1,5):
        data = np.load(filename + str(k) + '.npz')

        t = data['t']
        phi_e_n = data['phi_e_n']
        phi_e_g = data['phi_e_g']
        phi_e_diff = data['phi_e_diff']
        I_stim_ = data['I_stim']*1e12 # [pA]
        
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
        
        I_stim.append(I_stim_)
        mean_phi_e_n.append(mean_phi_e_n_)
        mean_phi_e_g.append(mean_phi_e_g_)
        mean_phi_e_diff.append(mean_phi_e_diff_)

    return I_stim, mean_phi_e_n, mean_phi_e_g, mean_phi_e_diff


t_thresh = 50
I_stim_K_soma_ss, n_K_soma_ss, g_K_soma_ss, diff_K_soma_ss = mean_phi('data/figure6_K_soma_ss_', t_thresh)
I_stim_K_dendrite_ss, n_K_dendrite_ss, g_K_dendrite_ss, diff_K_dendrite_ss = mean_phi('data/figure6_K_dendrite_ss_', t_thresh)
I_stim_K_both_ss, n_K_both_ss, g_K_both_ss, diff_K_both_ss = mean_phi('data/figure6_K_both_ss_', t_thresh)

I_stim_Na_soma_ss, n_Na_soma_ss, g_Na_soma_ss, diff_Na_soma_ss = mean_phi('data/figure6_Na_soma_ss_', t_thresh)
I_stim_Na_dendrite_ss, n_Na_dendrite_ss, g_Na_dendrite_ss, diff_Na_dendrite_ss = mean_phi('data/figure6_Na_dendrite_ss_', t_thresh)
I_stim_Na_both_ss, n_Na_both_ss, g_Na_both_ss, diff_Na_both_ss = mean_phi('data/figure6_Na_both_ss_', t_thresh)

I_stim_Cl_soma_ss, n_Cl_soma_ss, g_Cl_soma_ss, diff_Cl_soma_ss = mean_phi('data/figure6_Cl_soma_ss_', t_thresh)
I_stim_Cl_dendrite_ss, n_Cl_dendrite_ss, g_Cl_dendrite_ss, diff_Cl_dendrite_ss = mean_phi('data/figure6_Cl_dendrite_ss_', t_thresh)
I_stim_Cl_both_ss, n_Cl_both_ss, g_Cl_both_ss, diff_Cl_both_ss = mean_phi('data/figure6_Cl_both_ss_', t_thresh)

t_thresh = 590
I_stim_K_soma_db, n_K_soma_db, g_K_soma_db, diff_K_soma_db = mean_phi('data/figure6_K_soma_db_', t_thresh)
I_stim_K_dendrite_db, n_K_dendrite_db, g_K_dendrite_db, diff_K_dendrite_db = mean_phi('data/figure6_K_dendrite_db_', t_thresh)
I_stim_K_both_db, n_K_both_db, g_K_both_db, diff_K_both_db = mean_phi('data/figure6_K_both_db_', t_thresh)

I_stim_Na_soma_db, n_Na_soma_db, g_Na_soma_db, diff_Na_soma_db = mean_phi('data/figure6_Na_soma_db_', t_thresh)
I_stim_Na_dendrite_db, n_Na_dendrite_db, g_Na_dendrite_db, diff_Na_dendrite_db = mean_phi('data/figure6_Na_dendrite_db_', t_thresh)
I_stim_Na_both_db, n_Na_both_db, g_Na_both_db, diff_Na_both_db = mean_phi('data/figure6_Na_both_db_', t_thresh)

I_stim_Cl_soma_db, n_Cl_soma_db, g_Cl_soma_db, diff_Cl_soma_db = mean_phi('data/figure6_Cl_soma_db_', t_thresh)
I_stim_Cl_dendrite_db, n_Cl_dendrite_db, g_Cl_dendrite_db, diff_Cl_dendrite_db = mean_phi('data/figure6_Cl_dendrite_db_', t_thresh)
I_stim_Cl_both_db, n_Cl_both_db, g_Cl_both_db, diff_Cl_both_db = mean_phi('data/figure6_Cl_both_db_', t_thresh)

np.savez('data/figure6.npz', \
I_stim_K_soma_ss=I_stim_K_soma_ss, \
n_K_soma_ss=n_K_soma_ss, \
g_K_soma_ss=g_K_soma_ss, \
diff_K_soma_ss=diff_K_soma_ss, \
I_stim_K_dendrite_ss=I_stim_K_dendrite_ss, \
n_K_dendrite_ss=n_K_dendrite_ss, \
g_K_dendrite_ss=g_K_dendrite_ss, \
diff_K_dendrite_ss=diff_K_dendrite_ss, \
I_stim_K_both_ss=I_stim_K_both_ss, \
n_K_both_ss=n_K_both_ss, \
g_K_both_ss=g_K_both_ss, \
diff_K_both_ss=diff_K_both_ss, \
I_stim_K_soma_db=I_stim_K_soma_db, \
n_K_soma_db=n_K_soma_db, \
g_K_soma_db=g_K_soma_db, \
diff_K_soma_db=diff_K_soma_db, \
I_stim_K_dendrite_db=I_stim_K_dendrite_db, \
n_K_dendrite_db=n_K_dendrite_db, \
g_K_dendrite_db=g_K_dendrite_db, \
diff_K_dendrite_db=diff_K_dendrite_db, \
I_stim_K_both_db=I_stim_K_both_db, \
n_K_both_db=n_K_both_db, \
g_K_both_db=g_K_both_db, \
diff_K_both_db=diff_K_both_db, \
I_stim_Na_soma_ss=I_stim_Na_soma_ss, \
n_Na_soma_ss=n_Na_soma_ss, \
g_Na_soma_ss=g_Na_soma_ss, \
diff_Na_soma_ss=diff_Na_soma_ss, \
I_stim_Na_dendrite_ss=I_stim_Na_dendrite_ss, \
n_Na_dendrite_ss=n_Na_dendrite_ss, \
g_Na_dendrite_ss=g_Na_dendrite_ss, \
diff_Na_dendrite_ss=diff_Na_dendrite_ss, \
I_stim_Na_both_ss=I_stim_Na_both_ss, \
n_Na_both_ss=n_Na_both_ss, \
g_Na_both_ss=g_Na_both_ss, \
diff_Na_both_ss=diff_Na_both_ss, \
I_stim_Na_soma_db=I_stim_Na_soma_db, \
n_Na_soma_db=n_Na_soma_db, \
g_Na_soma_db=g_Na_soma_db, \
diff_Na_soma_db=diff_Na_soma_db, \
I_stim_Na_dendrite_db=I_stim_Na_dendrite_db, \
n_Na_dendrite_db=n_Na_dendrite_db, \
g_Na_dendrite_db=g_Na_dendrite_db, \
diff_Na_dendrite_db=diff_Na_dendrite_db, \
I_stim_Na_both_db=I_stim_Na_both_db, \
n_Na_both_db=n_Na_both_db, \
g_Na_both_db=g_Na_both_db, \
diff_Na_both_db=diff_Na_both_db, \
I_stim_Cl_soma_ss=I_stim_Cl_soma_ss, \
n_Cl_soma_ss=n_Cl_soma_ss, \
g_Cl_soma_ss=g_Cl_soma_ss, \
diff_Cl_soma_ss=diff_Cl_soma_ss, \
I_stim_Cl_dendrite_ss=I_stim_Cl_dendrite_ss, \
n_Cl_dendrite_ss=n_Cl_dendrite_ss, \
g_Cl_dendrite_ss=g_Cl_dendrite_ss, \
diff_Cl_dendrite_ss=diff_Cl_dendrite_ss, \
I_stim_Cl_both_ss=I_stim_Cl_both_ss, \
n_Cl_both_ss=n_Cl_both_ss, \
g_Cl_both_ss=g_Cl_both_ss, \
diff_Cl_both_ss=diff_Cl_both_ss, \
I_stim_Cl_soma_db=I_stim_Cl_soma_db, \
n_Cl_soma_db=n_Cl_soma_db, \
g_Cl_soma_db=g_Cl_soma_db, \
diff_Cl_soma_db=diff_Cl_soma_db, \
I_stim_Cl_dendrite_db=I_stim_Cl_dendrite_db, \
n_Cl_dendrite_db=n_Cl_dendrite_db, \
g_Cl_dendrite_db=g_Cl_dendrite_db, \
diff_Cl_dendrite_db=diff_Cl_dendrite_db, \
I_stim_Cl_both_db=I_stim_Cl_both_db, \
n_Cl_both_db=n_Cl_both_db, \
g_Cl_both_db=g_Cl_both_db, \
diff_Cl_both_db=diff_Cl_both_db)
