from brain_tissue_module.brain_tissue_module import *
import numpy as np
import time
from functions.solve_brain_tissue_module_figure7 import *

start_time = time.time()

I_stim = 320e-12 # [A]
alpha = 2
t_dur = 90       # [s]
stim_dur = 0.01  # [s]

module_version = 'with glia'
k = 1
for frequency in [1, 2, 3, 4, 5, 6, 7, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8, 9, 10]:
    interval = 1/frequency
    stim_start = np.arange(0.1, t_dur, interval)

    sol, my_cell = solve_brain_tissue_module_figure7(t_dur, alpha, I_stim, stim_start, stim_dur, module_version)
    t = sol.t

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    np.savez('data/figure7_with_glia_'+str(k), \
        t=t, \
        Na_sn=my_cell.Na_sn, Na_se=my_cell.Na_se, Na_sg=my_cell.Na_sg, \
        Na_dn=my_cell.Na_dn, Na_de=my_cell.Na_de, Na_dg=my_cell.Na_dg, \
        K_sn=my_cell.K_sn, K_se=my_cell.K_se, K_sg=my_cell.K_sg, \
        K_dn=my_cell.K_dn, K_de=my_cell.K_de, K_dg=my_cell.K_dg, \
        Cl_sn=my_cell.Cl_sn, Cl_se=my_cell.Cl_se, Cl_sg=my_cell.Cl_sg, \
        Cl_dn=my_cell.Cl_dn, Cl_de=my_cell.Cl_de, Cl_dg=my_cell.Cl_dg, \
        Ca_sn=my_cell.Ca_sn, Ca_se=my_cell.Ca_se, Ca_dn=my_cell.Ca_dn, Ca_de=my_cell.Ca_de, \
        cNa_sn=my_cell.cNa_sn, cNa_se=my_cell.cNa_se, cNa_sg=my_cell.cNa_sg, \
        cNa_dn=my_cell.cNa_dn, cNa_de=my_cell.cNa_de, cNa_dg=my_cell.cNa_dg, \
        cK_sn=my_cell.cK_sn, cK_se=my_cell.cK_se, cK_sg=my_cell.cK_sg, \
        cK_dn=my_cell.cK_dn, cK_de=my_cell.cK_de, cK_dg=my_cell.cK_dg, \
        cCl_sn=my_cell.cCl_sn, cCl_se=my_cell.cCl_se, cCl_sg=my_cell.cCl_sg, \
        cCl_dn=my_cell.cCl_dn, cCl_de=my_cell.cCl_de, cCl_dg=my_cell.cCl_dg, \
        cCa_sn=my_cell.cCa_sn, cCa_se=my_cell.cCa_se, cCa_dn=my_cell.cCa_dn, cCa_de=my_cell.cCa_de, \
        X_sn=my_cell.X_sn, X_se=my_cell.X_se, X_sg=my_cell.X_sg, \
        X_dn=my_cell.X_dn, X_de=my_cell.X_de, X_dg=my_cell.X_dg, \
        cX_sn=my_cell.cX_sn, cX_se=my_cell.cX_se, cX_sg=my_cell.cX_sg, \
        cX_dn=my_cell.cX_dn, cX_de=my_cell.cX_de, cX_dg=my_cell.cX_dg, \
        n=my_cell.n, h=my_cell.h, s=my_cell.s, c=my_cell.c, q=my_cell.q, z=my_cell.z, \
        V_sn=my_cell.V_sn, V_se=my_cell.V_se, V_sg=my_cell.V_sg, V_dn=my_cell.V_dn, V_de=my_cell.V_de, V_dg=my_cell.V_dg, \
        cM_sn=my_cell.cM_sn, cM_se=my_cell.cM_se, cM_sg=my_cell.cM_sg, \
        cM_dn=my_cell.cM_dn, cM_de=my_cell.cM_de, cM_dg=my_cell.cM_dg, \
        T = my_cell.T, \
        phi_sn=phi_sn, phi_se=phi_se, phi_sg=phi_sg, phi_dn=phi_dn, phi_de=phi_de, phi_dg=phi_dg, \
        phi_msn=phi_msn, phi_mdn=phi_mdn, phi_msg=phi_msg, phi_mdg=phi_mdg, \
        E_Na_sn=E_Na_sn, E_Na_sg=E_Na_sg, E_Na_dn=E_Na_dn, E_Na_dg=E_Na_dg, \
        E_K_sn=E_K_sn, E_K_sg=E_K_sg, E_K_dn=E_K_dn, E_K_dg=E_K_dg, \
        E_Cl_sn=E_Cl_sn, E_Cl_sg=E_Cl_sg, E_Cl_dn=E_Cl_dn, E_Cl_dg=E_Cl_dg, \
        E_Ca_sn=E_Ca_sn, E_Ca_dn=E_Ca_dn, I_stim=I_stim, alpha=alpha, \
        stimulus_frequency=frequency)
    k += 1

module_version = 'no glia'
k = 1
for frequency in [1, 2, 3, 4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5, 6, 7, 8, 9, 10]:
    interval = 1/frequency
    stim_start = np.arange(0.1, t_dur, interval)

    sol, my_cell = solve_brain_tissue_module_figure7(t_dur, alpha, I_stim, stim_start, stim_dur, module_version)
    t = sol.t

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    np.savez('data/figure7_no_glia_'+str(k), \
        t=t, \
        Na_sn=my_cell.Na_sn, Na_se=my_cell.Na_se, Na_sg=my_cell.Na_sg, \
        Na_dn=my_cell.Na_dn, Na_de=my_cell.Na_de, Na_dg=my_cell.Na_dg, \
        K_sn=my_cell.K_sn, K_se=my_cell.K_se, K_sg=my_cell.K_sg, \
        K_dn=my_cell.K_dn, K_de=my_cell.K_de, K_dg=my_cell.K_dg, \
        Cl_sn=my_cell.Cl_sn, Cl_se=my_cell.Cl_se, Cl_sg=my_cell.Cl_sg, \
        Cl_dn=my_cell.Cl_dn, Cl_de=my_cell.Cl_de, Cl_dg=my_cell.Cl_dg, \
        Ca_sn=my_cell.Ca_sn, Ca_se=my_cell.Ca_se, Ca_dn=my_cell.Ca_dn, Ca_de=my_cell.Ca_de, \
        cNa_sn=my_cell.cNa_sn, cNa_se=my_cell.cNa_se, cNa_sg=my_cell.cNa_sg, \
        cNa_dn=my_cell.cNa_dn, cNa_de=my_cell.cNa_de, cNa_dg=my_cell.cNa_dg, \
        cK_sn=my_cell.cK_sn, cK_se=my_cell.cK_se, cK_sg=my_cell.cK_sg, \
        cK_dn=my_cell.cK_dn, cK_de=my_cell.cK_de, cK_dg=my_cell.cK_dg, \
        cCl_sn=my_cell.cCl_sn, cCl_se=my_cell.cCl_se, cCl_sg=my_cell.cCl_sg, \
        cCl_dn=my_cell.cCl_dn, cCl_de=my_cell.cCl_de, cCl_dg=my_cell.cCl_dg, \
        cCa_sn=my_cell.cCa_sn, cCa_se=my_cell.cCa_se, cCa_dn=my_cell.cCa_dn, cCa_de=my_cell.cCa_de, \
        X_sn=my_cell.X_sn, X_se=my_cell.X_se, X_sg=my_cell.X_sg, \
        X_dn=my_cell.X_dn, X_de=my_cell.X_de, X_dg=my_cell.X_dg, \
        cX_sn=my_cell.cX_sn, cX_se=my_cell.cX_se, cX_sg=my_cell.cX_sg, \
        cX_dn=my_cell.cX_dn, cX_de=my_cell.cX_de, cX_dg=my_cell.cX_dg, \
        n=my_cell.n, h=my_cell.h, s=my_cell.s, c=my_cell.c, q=my_cell.q, z=my_cell.z, \
        V_sn=my_cell.V_sn, V_se=my_cell.V_se, V_sg=my_cell.V_sg, V_dn=my_cell.V_dn, V_de=my_cell.V_de, V_dg=my_cell.V_dg, \
        cM_sn=my_cell.cM_sn, cM_se=my_cell.cM_se, cM_sg=my_cell.cM_sg, cM_dn=my_cell.cM_dn, cM_de=my_cell.cM_de, cM_dg=my_cell.cM_dg, \
        T = my_cell.T, \
        phi_sn=phi_sn, phi_se=phi_se, phi_sg=phi_sg, phi_dn=phi_dn, phi_de=phi_de, phi_dg=phi_dg, \
        phi_msn=phi_msn, phi_mdn=phi_mdn, phi_msg=phi_msg, phi_mdg=phi_mdg, \
        E_Na_sn=E_Na_sn, E_Na_sg=E_Na_sg, E_Na_dn=E_Na_dn, E_Na_dg=E_Na_dg, \
        E_K_sn=E_K_sn, E_K_sg=E_K_sg, E_K_dn=E_K_dn, E_K_dg=E_K_dg, \
        E_Cl_sn=E_Cl_sn, E_Cl_sg=E_Cl_sg, E_Cl_dn=E_Cl_dn, E_Cl_dg=E_Cl_dg, \
        E_Ca_sn=E_Ca_sn, E_Ca_dn=E_Ca_dn, I_stim=I_stim, alpha=alpha, \
        stimulus_frequency=frequency)
    k += 1

module_version = 'with glia no swelling'
k = 1
for frequency in [1, 2, 3, 4, 5, 6, 7, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8, 9, 10]:
    interval = 1/frequency
    stim_start = np.arange(0.1, t_dur, interval)

    sol, my_cell = solve_brain_tissue_module_figure7(t_dur, alpha, I_stim, stim_start, stim_dur, module_version)
    t = sol.t

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    np.savez('data/figure7_with_glia_no_swelling_'+str(k), \
        t=t, \
        Na_sn=my_cell.Na_sn, Na_se=my_cell.Na_se, Na_sg=my_cell.Na_sg, \
        Na_dn=my_cell.Na_dn, Na_de=my_cell.Na_de, Na_dg=my_cell.Na_dg, \
        K_sn=my_cell.K_sn, K_se=my_cell.K_se, K_sg=my_cell.K_sg, \
        K_dn=my_cell.K_dn, K_de=my_cell.K_de, K_dg=my_cell.K_dg, \
        Cl_sn=my_cell.Cl_sn, Cl_se=my_cell.Cl_se, Cl_sg=my_cell.Cl_sg, \
        Cl_dn=my_cell.Cl_dn, Cl_de=my_cell.Cl_de, Cl_dg=my_cell.Cl_dg, \
        Ca_sn=my_cell.Ca_sn, Ca_se=my_cell.Ca_se, Ca_dn=my_cell.Ca_dn, Ca_de=my_cell.Ca_de, \
        cNa_sn=my_cell.cNa_sn, cNa_se=my_cell.cNa_se, cNa_sg=my_cell.cNa_sg, \
        cNa_dn=my_cell.cNa_dn, cNa_de=my_cell.cNa_de, cNa_dg=my_cell.cNa_dg, \
        cK_sn=my_cell.cK_sn, cK_se=my_cell.cK_se, cK_sg=my_cell.cK_sg, \
        cK_dn=my_cell.cK_dn, cK_de=my_cell.cK_de, cK_dg=my_cell.cK_dg, \
        cCl_sn=my_cell.cCl_sn, cCl_se=my_cell.cCl_se, cCl_sg=my_cell.cCl_sg, \
        cCl_dn=my_cell.cCl_dn, cCl_de=my_cell.cCl_de, cCl_dg=my_cell.cCl_dg, \
        cCa_sn=my_cell.cCa_sn, cCa_se=my_cell.cCa_se, cCa_dn=my_cell.cCa_dn, cCa_de=my_cell.cCa_de, \
        X_sn=my_cell.X_sn, X_se=my_cell.X_se, X_sg=my_cell.X_sg, \
        X_dn=my_cell.X_dn, X_de=my_cell.X_de, X_dg=my_cell.X_dg, \
        cX_sn=my_cell.cX_sn, cX_se=my_cell.cX_se, cX_sg=my_cell.cX_sg, \
        cX_dn=my_cell.cX_dn, cX_de=my_cell.cX_de, cX_dg=my_cell.cX_dg, \
        n=my_cell.n, h=my_cell.h, s=my_cell.s, c=my_cell.c, q=my_cell.q, z=my_cell.z, \
        V_sn=my_cell.V_sn, V_se=my_cell.V_se, V_sg=my_cell.V_sg, V_dn=my_cell.V_dn, V_de=my_cell.V_de, V_dg=my_cell.V_dg, \
        cM_sn=my_cell.cM_sn, cM_se=my_cell.cM_se, cM_sg=my_cell.cM_sg, \
        cM_dn=my_cell.cM_dn, cM_de=my_cell.cM_de, cM_dg=my_cell.cM_dg, \
        T = my_cell.T, \
        phi_sn=phi_sn, phi_se=phi_se, phi_sg=phi_sg, phi_dn=phi_dn, phi_de=phi_de, phi_dg=phi_dg, \
        phi_msn=phi_msn, phi_mdn=phi_mdn, phi_msg=phi_msg, phi_mdg=phi_mdg, \
        E_Na_sn=E_Na_sn, E_Na_sg=E_Na_sg, E_Na_dn=E_Na_dn, E_Na_dg=E_Na_dg, \
        E_K_sn=E_K_sn, E_K_sg=E_K_sg, E_K_dn=E_K_dn, E_K_dg=E_K_dg, \
        E_Cl_sn=E_Cl_sn, E_Cl_sg=E_Cl_sg, E_Cl_dn=E_Cl_dn, E_Cl_dg=E_Cl_dg, \
        E_Ca_sn=E_Ca_sn, E_Ca_dn=E_Ca_dn, I_stim=I_stim, alpha=alpha, \
        stimulus_frequency=frequency)
    k += 1

module_version = 'no glia no swelling'
k = 1
for frequency in [1, 2, 3, 4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5, 6, 7, 8, 9, 10]:
    interval = 1/frequency
    stim_start = np.arange(0.1, t_dur, interval)

    sol, my_cell = solve_brain_tissue_module_figure7(t_dur, alpha, I_stim, stim_start, stim_dur, module_version)
    t = sol.t

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    np.savez('data/figure7_no_glia_no_swelling_'+str(k), \
        t=t, \
        Na_sn=my_cell.Na_sn, Na_se=my_cell.Na_se, Na_sg=my_cell.Na_sg, \
        Na_dn=my_cell.Na_dn, Na_de=my_cell.Na_de, Na_dg=my_cell.Na_dg, \
        K_sn=my_cell.K_sn, K_se=my_cell.K_se, K_sg=my_cell.K_sg, \
        K_dn=my_cell.K_dn, K_de=my_cell.K_de, K_dg=my_cell.K_dg, \
        Cl_sn=my_cell.Cl_sn, Cl_se=my_cell.Cl_se, Cl_sg=my_cell.Cl_sg, \
        Cl_dn=my_cell.Cl_dn, Cl_de=my_cell.Cl_de, Cl_dg=my_cell.Cl_dg, \
        Ca_sn=my_cell.Ca_sn, Ca_se=my_cell.Ca_se, Ca_dn=my_cell.Ca_dn, Ca_de=my_cell.Ca_de, \
        cNa_sn=my_cell.cNa_sn, cNa_se=my_cell.cNa_se, cNa_sg=my_cell.cNa_sg, \
        cNa_dn=my_cell.cNa_dn, cNa_de=my_cell.cNa_de, cNa_dg=my_cell.cNa_dg, \
        cK_sn=my_cell.cK_sn, cK_se=my_cell.cK_se, cK_sg=my_cell.cK_sg, \
        cK_dn=my_cell.cK_dn, cK_de=my_cell.cK_de, cK_dg=my_cell.cK_dg, \
        cCl_sn=my_cell.cCl_sn, cCl_se=my_cell.cCl_se, cCl_sg=my_cell.cCl_sg, \
        cCl_dn=my_cell.cCl_dn, cCl_de=my_cell.cCl_de, cCl_dg=my_cell.cCl_dg, \
        cCa_sn=my_cell.cCa_sn, cCa_se=my_cell.cCa_se, cCa_dn=my_cell.cCa_dn, cCa_de=my_cell.cCa_de, \
        X_sn=my_cell.X_sn, X_se=my_cell.X_se, X_sg=my_cell.X_sg, \
        X_dn=my_cell.X_dn, X_de=my_cell.X_de, X_dg=my_cell.X_dg, \
        cX_sn=my_cell.cX_sn, cX_se=my_cell.cX_se, cX_sg=my_cell.cX_sg, \
        cX_dn=my_cell.cX_dn, cX_de=my_cell.cX_de, cX_dg=my_cell.cX_dg, \
        n=my_cell.n, h=my_cell.h, s=my_cell.s, c=my_cell.c, q=my_cell.q, z=my_cell.z, \
        V_sn=my_cell.V_sn, V_se=my_cell.V_se, V_sg=my_cell.V_sg, V_dn=my_cell.V_dn, V_de=my_cell.V_de, V_dg=my_cell.V_dg, \
        cM_sn=my_cell.cM_sn, cM_se=my_cell.cM_se, cM_sg=my_cell.cM_sg, cM_dn=my_cell.cM_dn, cM_de=my_cell.cM_de, cM_dg=my_cell.cM_dg, \
        T = my_cell.T, \
        phi_sn=phi_sn, phi_se=phi_se, phi_sg=phi_sg, phi_dn=phi_dn, phi_de=phi_de, phi_dg=phi_dg, \
        phi_msn=phi_msn, phi_mdn=phi_mdn, phi_msg=phi_msg, phi_mdg=phi_mdg, \
        E_Na_sn=E_Na_sn, E_Na_sg=E_Na_sg, E_Na_dn=E_Na_dn, E_Na_dg=E_Na_dg, \
        E_K_sn=E_K_sn, E_K_sg=E_K_sg, E_K_dn=E_K_dn, E_K_dg=E_K_dg, \
        E_Cl_sn=E_Cl_sn, E_Cl_sg=E_Cl_sg, E_Cl_dn=E_Cl_dn, E_Cl_dg=E_Cl_dg, \
        E_Ca_sn=E_Ca_sn, E_Ca_dn=E_Ca_dn, I_stim=I_stim, alpha=alpha, \
        stimulus_frequency=frequency)
    k += 1
