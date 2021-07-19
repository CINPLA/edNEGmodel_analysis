import numpy as np
from edNEGmodel.edNEGmodel import *
from functions.solve_edNEGmodel_figure7 import *
from functions.split_phi_e__synaptic_stimuli import *
from functions.print_final_values import *

alpha = 2
syn_start = 1    # [s]
syn_end = 60     # [s]

# soma
syn_protocol = 'syn_soma'
dendritic_synapse = False 
t_dur = 60       # [s]
k = 1
for syn_rate in range(300, 601, 100):
    sol, my_cell, spikes = solve_edNEGmodel(t_dur, alpha, syn_rate, syn_start, syn_end, syn_protocol)

    t = sol.t

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    phi_e_n, phi_e_g, phi_e_diff = split_phi_e(my_cell, t, spikes, dendritic_synapse)

    np.savez('data/figure7_syn_soma_ss_' + str(k), t=t, phi_sn=phi_sn, phi_se=phi_se, phi_dn=phi_dn, phi_de=phi_de, phi_sg=phi_sg, phi_dg=phi_dg, \
        phi_msn=phi_msn, phi_mdn=phi_mdn, phi_msg=phi_msg, phi_mdg=phi_mdg, \
        E_Na_sn=E_Na_sn, E_Na_dn=E_Na_dn, E_Na_sg=E_Na_sg, E_Na_dg=E_Na_dg, \
        E_K_sn=E_K_sn, E_K_dn=E_K_dn, E_K_sg=E_K_sg, E_K_dg=E_K_dg, \
        E_Cl_sn=E_Cl_sn, E_Cl_dn=E_Cl_dn, E_Cl_sg=E_Cl_sg, E_Cl_dg=E_Cl_dg, \
        E_Ca_sn=E_Ca_sn, E_Ca_dn=E_Ca_dn, \
        cNa_sn=my_cell.cNa_sn, cNa_se=my_cell.cNa_se, cNa_sg=my_cell.cNa_sg, cNa_dn=my_cell.cNa_dn, cNa_de=my_cell.cNa_de, cNa_dg=my_cell.cNa_dg, \
        cK_sn=my_cell.cK_sn, cK_se=my_cell.cK_se, cK_sg=my_cell.cK_sg, cK_dn=my_cell.cK_dn, cK_de=my_cell.cK_de, cK_dg=my_cell.cK_dg, \
        cCl_sn=my_cell.cCl_sn, cCl_se=my_cell.cCl_se, cCl_sg=my_cell.cCl_sg, cCl_dn=my_cell.cCl_dn, cCl_de=my_cell.cCl_de, cCl_dg=my_cell.cCl_dg, \
        cCa_sn=my_cell.cCa_sn, cCa_se=my_cell.cCa_se, cCa_dn=my_cell.cCa_dn, cCa_de=my_cell.cCa_de, \
        free_cCa_dn=my_cell.free_cCa_dn, \
        V_sn = my_cell.V_sn, V_se = my_cell.V_se, V_sg = my_cell.V_sg, \
        V_dn = my_cell.V_dn, V_de = my_cell.V_de, V_dg = my_cell.V_dg, \
        phi_e_n=phi_e_n, phi_e_g=phi_e_g, phi_e_diff=phi_e_diff, syn_rate=syn_rate)

    k += 1

t_dur = 600       # [s]
k = 1
for syn_rate in range(700, 1001, 100):
    sol, my_cell, spikes = solve_edNEGmodel(t_dur, alpha, syn_rate, syn_start, syn_end, syn_protocol)

    t = sol.t

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    phi_e_n, phi_e_g, phi_e_diff = split_phi_e(my_cell, t, spikes, dendritic_synapse)

    np.savez('data/figure7_syn_soma_db_' + str(k), t=t, phi_sn=phi_sn, phi_se=phi_se, phi_dn=phi_dn, phi_de=phi_de, phi_sg=phi_sg, phi_dg=phi_dg, \
        phi_msn=phi_msn, phi_mdn=phi_mdn, phi_msg=phi_msg, phi_mdg=phi_mdg, \
        E_Na_sn=E_Na_sn, E_Na_dn=E_Na_dn, E_Na_sg=E_Na_sg, E_Na_dg=E_Na_dg, \
        E_K_sn=E_K_sn, E_K_dn=E_K_dn, E_K_sg=E_K_sg, E_K_dg=E_K_dg, \
        E_Cl_sn=E_Cl_sn, E_Cl_dn=E_Cl_dn, E_Cl_sg=E_Cl_sg, E_Cl_dg=E_Cl_dg, \
        E_Ca_sn=E_Ca_sn, E_Ca_dn=E_Ca_dn, \
        cNa_sn=my_cell.cNa_sn, cNa_se=my_cell.cNa_se, cNa_sg=my_cell.cNa_sg, cNa_dn=my_cell.cNa_dn, cNa_de=my_cell.cNa_de, cNa_dg=my_cell.cNa_dg, \
        cK_sn=my_cell.cK_sn, cK_se=my_cell.cK_se, cK_sg=my_cell.cK_sg, cK_dn=my_cell.cK_dn, cK_de=my_cell.cK_de, cK_dg=my_cell.cK_dg, \
        cCl_sn=my_cell.cCl_sn, cCl_se=my_cell.cCl_se, cCl_sg=my_cell.cCl_sg, cCl_dn=my_cell.cCl_dn, cCl_de=my_cell.cCl_de, cCl_dg=my_cell.cCl_dg, \
        cCa_sn=my_cell.cCa_sn, cCa_se=my_cell.cCa_se, cCa_dn=my_cell.cCa_dn, cCa_de=my_cell.cCa_de, \
        free_cCa_dn=my_cell.free_cCa_dn, \
        V_sn = my_cell.V_sn, V_se = my_cell.V_se, V_sg = my_cell.V_sg, \
        V_dn = my_cell.V_dn, V_de = my_cell.V_de, V_dg = my_cell.V_dg, \
        phi_e_n=phi_e_n, phi_e_g=phi_e_g, phi_e_diff=phi_e_diff, syn_rate=syn_rate)

    k += 1

# dendrite
syn_protocol = 'syn_dendrite'
dendritic_synapse = True 
t_dur = 60       # [s]
k = 1
for syn_rate in range(400, 701, 100):
    sol, my_cell, spikes = solve_edNEGmodel(t_dur, alpha, syn_rate, syn_start, syn_end, syn_protocol)

    t = sol.t

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    phi_e_n, phi_e_g, phi_e_diff = split_phi_e(my_cell, t, spikes, dendritic_synapse)

    np.savez('data/figure7_syn_dendrite_ss_' + str(k), t=t, phi_sn=phi_sn, phi_se=phi_se, phi_dn=phi_dn, phi_de=phi_de, phi_sg=phi_sg, phi_dg=phi_dg, \
        phi_msn=phi_msn, phi_mdn=phi_mdn, phi_msg=phi_msg, phi_mdg=phi_mdg, \
        E_Na_sn=E_Na_sn, E_Na_dn=E_Na_dn, E_Na_sg=E_Na_sg, E_Na_dg=E_Na_dg, \
        E_K_sn=E_K_sn, E_K_dn=E_K_dn, E_K_sg=E_K_sg, E_K_dg=E_K_dg, \
        E_Cl_sn=E_Cl_sn, E_Cl_dn=E_Cl_dn, E_Cl_sg=E_Cl_sg, E_Cl_dg=E_Cl_dg, \
        E_Ca_sn=E_Ca_sn, E_Ca_dn=E_Ca_dn, \
        cNa_sn=my_cell.cNa_sn, cNa_se=my_cell.cNa_se, cNa_sg=my_cell.cNa_sg, cNa_dn=my_cell.cNa_dn, cNa_de=my_cell.cNa_de, cNa_dg=my_cell.cNa_dg, \
        cK_sn=my_cell.cK_sn, cK_se=my_cell.cK_se, cK_sg=my_cell.cK_sg, cK_dn=my_cell.cK_dn, cK_de=my_cell.cK_de, cK_dg=my_cell.cK_dg, \
        cCl_sn=my_cell.cCl_sn, cCl_se=my_cell.cCl_se, cCl_sg=my_cell.cCl_sg, cCl_dn=my_cell.cCl_dn, cCl_de=my_cell.cCl_de, cCl_dg=my_cell.cCl_dg, \
        cCa_sn=my_cell.cCa_sn, cCa_se=my_cell.cCa_se, cCa_dn=my_cell.cCa_dn, cCa_de=my_cell.cCa_de, \
        free_cCa_dn=my_cell.free_cCa_dn, \
        V_sn = my_cell.V_sn, V_se = my_cell.V_se, V_sg = my_cell.V_sg, \
        V_dn = my_cell.V_dn, V_de = my_cell.V_de, V_dg = my_cell.V_dg, \
        phi_e_n=phi_e_n, phi_e_g=phi_e_g, phi_e_diff=phi_e_diff, syn_rate=syn_rate)

    k += 1

t_dur = 600       # [s]
k = 1
for syn_rate in range(800, 1101, 100):
    sol, my_cell, spikes = solve_edNEGmodel(t_dur, alpha, syn_rate, syn_start, syn_end, syn_protocol)

    t = sol.t

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    phi_e_n, phi_e_g, phi_e_diff = split_phi_e(my_cell, t, spikes, dendritic_synapse)

    np.savez('data/figure7_syn_dendrite_db_' + str(k), t=t, phi_sn=phi_sn, phi_se=phi_se, phi_dn=phi_dn, phi_de=phi_de, phi_sg=phi_sg, phi_dg=phi_dg, \
        phi_msn=phi_msn, phi_mdn=phi_mdn, phi_msg=phi_msg, phi_mdg=phi_mdg, \
        E_Na_sn=E_Na_sn, E_Na_dn=E_Na_dn, E_Na_sg=E_Na_sg, E_Na_dg=E_Na_dg, \
        E_K_sn=E_K_sn, E_K_dn=E_K_dn, E_K_sg=E_K_sg, E_K_dg=E_K_dg, \
        E_Cl_sn=E_Cl_sn, E_Cl_dn=E_Cl_dn, E_Cl_sg=E_Cl_sg, E_Cl_dg=E_Cl_dg, \
        E_Ca_sn=E_Ca_sn, E_Ca_dn=E_Ca_dn, \
        cNa_sn=my_cell.cNa_sn, cNa_se=my_cell.cNa_se, cNa_sg=my_cell.cNa_sg, cNa_dn=my_cell.cNa_dn, cNa_de=my_cell.cNa_de, cNa_dg=my_cell.cNa_dg, \
        cK_sn=my_cell.cK_sn, cK_se=my_cell.cK_se, cK_sg=my_cell.cK_sg, cK_dn=my_cell.cK_dn, cK_de=my_cell.cK_de, cK_dg=my_cell.cK_dg, \
        cCl_sn=my_cell.cCl_sn, cCl_se=my_cell.cCl_se, cCl_sg=my_cell.cCl_sg, cCl_dn=my_cell.cCl_dn, cCl_de=my_cell.cCl_de, cCl_dg=my_cell.cCl_dg, \
        cCa_sn=my_cell.cCa_sn, cCa_se=my_cell.cCa_se, cCa_dn=my_cell.cCa_dn, cCa_de=my_cell.cCa_de, \
        free_cCa_dn=my_cell.free_cCa_dn, \
        V_sn = my_cell.V_sn, V_se = my_cell.V_se, V_sg = my_cell.V_sg, \
        V_dn = my_cell.V_dn, V_de = my_cell.V_de, V_dg = my_cell.V_dg, \
        phi_e_n=phi_e_n, phi_e_g=phi_e_g, phi_e_diff=phi_e_diff, syn_rate=syn_rate)

    k += 1

# both
syn_protocol = 'syn_both'
dendritic_synapse = False 
t_dur = 60       # [s]
k = 1
for syn_rate in range(150, 301, 50):
    sol, my_cell, spikes = solve_edNEGmodel(t_dur, alpha, syn_rate, syn_start, syn_end, syn_protocol)

    t = sol.t

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    phi_e_n, phi_e_g, phi_e_diff = split_phi_e(my_cell, t, spikes, dendritic_synapse)

    np.savez('data/figure7_syn_both_ss_' + str(k), t=t, phi_sn=phi_sn, phi_se=phi_se, phi_dn=phi_dn, phi_de=phi_de, phi_sg=phi_sg, phi_dg=phi_dg, \
        phi_msn=phi_msn, phi_mdn=phi_mdn, phi_msg=phi_msg, phi_mdg=phi_mdg, \
        E_Na_sn=E_Na_sn, E_Na_dn=E_Na_dn, E_Na_sg=E_Na_sg, E_Na_dg=E_Na_dg, \
        E_K_sn=E_K_sn, E_K_dn=E_K_dn, E_K_sg=E_K_sg, E_K_dg=E_K_dg, \
        E_Cl_sn=E_Cl_sn, E_Cl_dn=E_Cl_dn, E_Cl_sg=E_Cl_sg, E_Cl_dg=E_Cl_dg, \
        E_Ca_sn=E_Ca_sn, E_Ca_dn=E_Ca_dn, \
        cNa_sn=my_cell.cNa_sn, cNa_se=my_cell.cNa_se, cNa_sg=my_cell.cNa_sg, cNa_dn=my_cell.cNa_dn, cNa_de=my_cell.cNa_de, cNa_dg=my_cell.cNa_dg, \
        cK_sn=my_cell.cK_sn, cK_se=my_cell.cK_se, cK_sg=my_cell.cK_sg, cK_dn=my_cell.cK_dn, cK_de=my_cell.cK_de, cK_dg=my_cell.cK_dg, \
        cCl_sn=my_cell.cCl_sn, cCl_se=my_cell.cCl_se, cCl_sg=my_cell.cCl_sg, cCl_dn=my_cell.cCl_dn, cCl_de=my_cell.cCl_de, cCl_dg=my_cell.cCl_dg, \
        cCa_sn=my_cell.cCa_sn, cCa_se=my_cell.cCa_se, cCa_dn=my_cell.cCa_dn, cCa_de=my_cell.cCa_de, \
        free_cCa_dn=my_cell.free_cCa_dn, \
        V_sn = my_cell.V_sn, V_se = my_cell.V_se, V_sg = my_cell.V_sg, \
        V_dn = my_cell.V_dn, V_de = my_cell.V_de, V_dg = my_cell.V_dg, \
        phi_e_n=phi_e_n, phi_e_g=phi_e_g, phi_e_diff=phi_e_diff, syn_rate=syn_rate)

    k += 1

t_dur = 600       # [s]
k = 1
for syn_rate in range(350, 501, 50):
    sol, my_cell, spikes = solve_edNEGmodel(t_dur, alpha, syn_rate, syn_start, syn_end, syn_protocol)

    t = sol.t

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    phi_e_n, phi_e_g, phi_e_diff = split_phi_e(my_cell, t, spikes, dendritic_synapse)

    np.savez('data/figure7_syn_both_db_' + str(k), t=t, phi_sn=phi_sn, phi_se=phi_se, phi_dn=phi_dn, phi_de=phi_de, phi_sg=phi_sg, phi_dg=phi_dg, \
        phi_msn=phi_msn, phi_mdn=phi_mdn, phi_msg=phi_msg, phi_mdg=phi_mdg, \
        E_Na_sn=E_Na_sn, E_Na_dn=E_Na_dn, E_Na_sg=E_Na_sg, E_Na_dg=E_Na_dg, \
        E_K_sn=E_K_sn, E_K_dn=E_K_dn, E_K_sg=E_K_sg, E_K_dg=E_K_dg, \
        E_Cl_sn=E_Cl_sn, E_Cl_dn=E_Cl_dn, E_Cl_sg=E_Cl_sg, E_Cl_dg=E_Cl_dg, \
        E_Ca_sn=E_Ca_sn, E_Ca_dn=E_Ca_dn, \
        cNa_sn=my_cell.cNa_sn, cNa_se=my_cell.cNa_se, cNa_sg=my_cell.cNa_sg, cNa_dn=my_cell.cNa_dn, cNa_de=my_cell.cNa_de, cNa_dg=my_cell.cNa_dg, \
        cK_sn=my_cell.cK_sn, cK_se=my_cell.cK_se, cK_sg=my_cell.cK_sg, cK_dn=my_cell.cK_dn, cK_de=my_cell.cK_de, cK_dg=my_cell.cK_dg, \
        cCl_sn=my_cell.cCl_sn, cCl_se=my_cell.cCl_se, cCl_sg=my_cell.cCl_sg, cCl_dn=my_cell.cCl_dn, cCl_de=my_cell.cCl_de, cCl_dg=my_cell.cCl_dg, \
        cCa_sn=my_cell.cCa_sn, cCa_se=my_cell.cCa_se, cCa_dn=my_cell.cCa_dn, cCa_de=my_cell.cCa_de, \
        free_cCa_dn=my_cell.free_cCa_dn, \
        V_sn = my_cell.V_sn, V_se = my_cell.V_se, V_sg = my_cell.V_sg, \
        V_dn = my_cell.V_dn, V_de = my_cell.V_de, V_dg = my_cell.V_dg, \
        phi_e_n=phi_e_n, phi_e_g=phi_e_g, phi_e_diff=phi_e_diff, syn_rate=syn_rate)

    k += 1
