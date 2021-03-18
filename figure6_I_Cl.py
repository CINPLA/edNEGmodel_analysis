import numpy as np
from edNEGmodel.edNEGmodel import *
from functions.solve_edNEGmodel_figure6 import *
from functions.split_phi_e__injection_stimuli import *

alpha = 2

# Physiological activity 
t_dur = 60      # [s]
stim_start = 1  # [s]
stim_end = 60   # [s]

injection_protocol = 'Cl_soma_ss'
dendritic_stimuli = False 
k = 1
for I_stim_ in range(50, 90, 10):
    I_stim = I_stim_*1e-12
    sol, my_cell = solve_edNEGmodel(t_dur, alpha, I_stim, stim_start, stim_end, injection_protocol)

    t = sol.t

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    phi_e_n, phi_e_g, phi_e_diff = split_phi_e(my_cell, t, I_stim, stim_start, stim_end, dendritic_stimuli)

    np.savez('data/figure6_Cl_soma_ss_' + str(k), t=t, phi_sn=phi_sn, phi_se=phi_se, phi_dn=phi_dn, phi_de=phi_de, phi_sg=phi_sg, phi_dg=phi_dg, \
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
        phi_e_n=phi_e_n, phi_e_g=phi_e_g, phi_e_diff=phi_e_diff, I_stim=I_stim)

    k += 1

injection_protocol = 'Cl_dendrite_ss'
dendritic_stimuli = True 
k = 1
for I_stim_ in range(50, 90, 10):
    I_stim = I_stim_*1e-12
    sol, my_cell = solve_edNEGmodel(t_dur, alpha, I_stim, stim_start, stim_end, injection_protocol)

    t = sol.t

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    phi_e_n, phi_e_g, phi_e_diff = split_phi_e(my_cell, t, I_stim, stim_start, stim_end, dendritic_stimuli)

    np.savez('data/figure6_Cl_dendrite_ss_' + str(k), t=t, phi_sn=phi_sn, phi_se=phi_se, phi_dn=phi_dn, phi_de=phi_de, phi_sg=phi_sg, phi_dg=phi_dg, \
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
        phi_e_n=phi_e_n, phi_e_g=phi_e_g, phi_e_diff=phi_e_diff, I_stim=I_stim)

    k += 1

injection_protocol = 'Cl_both_ss'
dendritic_stimuli = True 
k = 1
for I_stim_ in range(10, 50, 10):
    I_stim = I_stim_*1e-12
    sol, my_cell = solve_edNEGmodel(t_dur, alpha, I_stim, stim_start, stim_end, injection_protocol)

    t = sol.t

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    phi_e_n, phi_e_g, phi_e_diff = split_phi_e(my_cell, t, I_stim, stim_start, stim_end, dendritic_stimuli)

    np.savez('data/figure6_Cl_both_ss_' + str(k), t=t, phi_sn=phi_sn, phi_se=phi_se, phi_dn=phi_dn, phi_de=phi_de, phi_sg=phi_sg, phi_dg=phi_dg, \
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
        phi_e_n=phi_e_n, phi_e_g=phi_e_g, phi_e_diff=phi_e_diff, I_stim=I_stim)

    k += 1

# Pathological activity
t_dur = 600     # [s]
stim_start = 1  # [s]
stim_end = 60   # [s]

injection_protocol = 'Cl_soma_db'
dendritic_stimuli = False 
k = 1
for I_stim_ in range(90, 121, 10):
    I_stim = I_stim_*1e-12
    sol, my_cell = solve_edNEGmodel(t_dur, alpha, I_stim, stim_start, stim_end, injection_protocol)

    t = sol.t

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    phi_e_n, phi_e_g, phi_e_diff = split_phi_e(my_cell, t, I_stim, stim_start, stim_end, dendritic_stimuli)

    np.savez('data/figure6_Cl_soma_db_' + str(k), t=t, phi_sn=phi_sn, phi_se=phi_se, phi_dn=phi_dn, phi_de=phi_de, phi_sg=phi_sg, phi_dg=phi_dg, \
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
        phi_e_n=phi_e_n, phi_e_g=phi_e_g, phi_e_diff=phi_e_diff, I_stim=I_stim)

    k += 1

injection_protocol = 'Cl_dendrite_db'
dendritic_stimuli = True 
k = 1
for I_stim_ in range(90, 121, 10):
    I_stim = I_stim_*1e-12
    sol, my_cell = solve_edNEGmodel(t_dur, alpha, I_stim, stim_start, stim_end, injection_protocol)

    t = sol.t

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    phi_e_n, phi_e_g, phi_e_diff = split_phi_e(my_cell, t, I_stim, stim_start, stim_end, dendritic_stimuli)

    np.savez('data/figure6_Cl_dendrite_db_' + str(k), t=t, phi_sn=phi_sn, phi_se=phi_se, phi_dn=phi_dn, phi_de=phi_de, phi_sg=phi_sg, phi_dg=phi_dg, \
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
        phi_e_n=phi_e_n, phi_e_g=phi_e_g, phi_e_diff=phi_e_diff, I_stim=I_stim)

    k += 1

injection_protocol = 'Cl_both_db'
dendritic_stimuli = True 
k = 1
for I_stim_ in range(50, 81, 10):
    I_stim = I_stim_*1e-12
    sol, my_cell = solve_edNEGmodel(t_dur, alpha, I_stim, stim_start, stim_end, injection_protocol)

    t = sol.t

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    phi_e_n, phi_e_g, phi_e_diff = split_phi_e(my_cell, t, I_stim, stim_start, stim_end, dendritic_stimuli)

    np.savez('data/figure6_Cl_both_db_' + str(k), t=t, phi_sn=phi_sn, phi_se=phi_se, phi_dn=phi_dn, phi_de=phi_de, phi_sg=phi_sg, phi_dg=phi_dg, \
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
        phi_e_n=phi_e_n, phi_e_g=phi_e_g, phi_e_diff=phi_e_diff, I_stim=I_stim)

    k += 1

